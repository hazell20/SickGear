# coding=utf-8
#
# This file is part of SickGear.
#
# SickGear is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SickGear is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SickGear.  If not, see <http://www.gnu.org/licenses/>.

import base64
import re
import traceback
import urllib

from . import generic
from sickbeard import logger
from sickbeard.bs4_parser import BS4Parser
from sickbeard.helpers import tryInt
from lib.unidecode import unidecode


class TorLockProvider(generic.TorrentProvider):

    def __init__(self):
        generic.TorrentProvider.__init__(self, 'TorLock')

        self.url_home = ['https://www.torlock.com/'] + \
                        ['https://%s/' % base64.b64decode(x) for x in [''.join(x) for x in [
                            [re.sub('[o\sH]+', '', x[::-1]) for x in [
                                'y9HHGd', 'j 9Gob', '1H5 ya', 'sJmoHb', 'rHNH2b', 'uQWo Z', '0Vm HY']],
                            [re.sub('[w\sm]+', '', x[::-1]) for x in [
                                'bym9mGd', 'ya jw9G', '02wbjw1', 'vJwHmcu', 'cwz5 Ce', 'QwZjmFG', '=  =']],
                            [re.sub('[N\sS]+', '', x[::-1]) for x in [
                                'y 9 Gd', 'j9SGNb', 'jN1 ya', 'u0N2Nb', 'vlNNWd', 'hNSZmL', 'o NRXa']],
                            [re.sub('[l\sO]+', '', x[::-1]) for x in [
                                'bylBD d', 'zajO9lG', '5lWdu E', 'j9OGb i', 'LkOV2Oa', 'A bvlxm', '=OO=']],
                            [re.sub('[o\ss]+', '', x[::-1]) for x in [
                                'bsyBDsd', 'zasj9oG', '5sWdsuE', 'j 9Gboi', 'LksV2oa', 'A sbvxm', '=s =']],
                            [re.sub('[q\sK]+', '', x[::-1]) for x in [
                                'yqq9Gd', 'j9 Gqb', '15qy a', 'sJKmKb', 'rNqq2b', 'uQqqWZ', '=gX Kb']],
                            [re.sub('[w\sI]+', '', x[::-1]) for x in [
                                'XwId', 'sI B', '2wIb', 'kI F', 'nI L', 'hIwB', 'nIwc', '5I R']],
                            [re.sub('[n\sP]+', '', x[::-1]) for x in [
                                'G nd', 'v nx', '2PPY', 'uPPs', 'GPPc', 'yPPF', 'Hnnd', '= nk']],
                        ]]]

        self.url_vars = {'search': 'television/torrents/%s.html?sort=added&order=desc',
                         'browse': 'television/1/added/desc.html', 'get': 'tor/%s.torrent'}
        self.url_tmpl = {'config_provider_home_uri': '%(home)s', 'search': '%(home)s%(vars)s',
                         'browse': '%(home)s%(vars)s', 'get': '%(home)s%(vars)s'}

        self.minseed, self.minleech = 2 * [None]
        self.confirmed = False

    @staticmethod
    def _has_signature(data=None):
        return data and re.search(r'(?i)TorLock', data[33:1024:])

    def _search_provider(self, search_params, **kwargs):

        results = []
        if not self.url:
            return results

        items = {'Cache': [], 'Season': [], 'Episode': [], 'Propers': []}

        rc = dict((k, re.compile('(?i)' + v)) for (k, v) in {
            'info': 'torrent.?(\d+)', 'versrc': r'ver\.', 'verified': 'Verified'}.iteritems())

        for mode in search_params.keys():
            for search_string in search_params[mode]:

                search_string = isinstance(search_string, unicode) and unidecode(search_string) or search_string

                search_url = self.urls['browse'] if 'Cache' == mode \
                    else self.urls['search'] % (urllib.quote_plus(search_string).replace('+', '-'))

                html = self.get_url(search_url)
                if self.should_skip():
                    return results

                cnt = len(items[mode])
                try:
                    if not html or self._has_no_results(html):
                        raise generic.HaltParseException
                    with BS4Parser(html, features=['html5lib', 'permissive']) as soup:

                        torrent_table = soup.find(
                            'div', class_=('panel panel-default', 'table-responsive')['Cache' == mode])
                        if None is torrent_table:
                            raise generic.HaltParseException
                        torrent_table = torrent_table.find(
                            'table', class_='table table-striped table-bordered table-hover table-condensed')
                        torrent_rows = [] if not torrent_table else torrent_table.find_all('tr')

                        if 2 > len(torrent_rows):
                            raise generic.HaltParseException

                        head = None
                        for tr in torrent_rows[1:]:
                            cells = tr.find_all('td')
                            if 5 > len(cells):
                                continue
                            try:
                                head = head if None is not head else self._header_row(tr)
                                seeders, leechers, size = [tryInt(n, n) for n in [
                                    cells[head[x]].get_text().strip() for x in 'seed', 'leech', 'size']]
                                if self._peers_fail(mode, seeders, leechers) \
                                        or self.confirmed and not (tr.find('img', src=rc['versrc'])
                                                                   or tr.find('img', title=rc['verified'])):
                                    continue

                                info = tr.find('a', href=rc['info']) or {}
                                title = info and info.get_text().strip()
                                tid_href = info and tryInt(rc['info'].findall(info['href'])[0])
                                download_url = tid_href and self._link(tid_href)
                            except (AttributeError, TypeError, ValueError, IndexError):
                                continue

                            if title and download_url:
                                items[mode].append((title, download_url, seeders, self._bytesizer(size)))

                except generic.HaltParseException:
                    pass
                except (StandardError, Exception):
                    logger.log(u'Failed to parse. Traceback: %s' % traceback.format_exc(), logger.ERROR)

                self._log_search(mode, len(items[mode]) - cnt, search_url)

            results = self._sort_seeding(mode, results + items[mode])

        return results


provider = TorLockProvider()
