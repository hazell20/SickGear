#
# fourcc are codes to specify the encoding method a audio or video string
# in RIFF file (.avi and .wav).
#
# The following lists come from mmpython project:
#    file: mmpython/video/fourcc.py
#    url:  http://sourceforge.net/projects/mmpython/
#

# List of codecs with no compression (compression rate=1.0)
UNCOMPRESSED_AUDIO = set((1, 3, 6))

audio_codec_name = {
    0x0000: u'Microsoft Unknown Wave Format',
    0x0001: u'Microsoft Pulse Code Modulation (PCM)',
    0x0002: u'Microsoft ADPCM',
    0x0003: u'IEEE Float',
    0x0004: u'Compaq Computer VSELP',
    0x0005: u'IBM CVSD',
    0x0006: u'Microsoft A-Law',
    0x0007: u'Microsoft mu-Law',
    0x0010: u'OKI ADPCM',
    0x0011: u'Intel DVI/IMA ADPCM',
    0x0012: u'Videologic MediaSpace ADPCM',
    0x0013: u'Sierra Semiconductor ADPCM',
    0x0014: u'Antex Electronics G.723 ADPCM',
    0x0015: u'DSP Solutions DigiSTD',
    0x0016: u'DSP Solutions DigiFIX',
    0x0017: u'Dialogic OKI ADPCM',
    0x0018: u'MediaVision ADPCM',
    0x0019: u'Hewlett-Packard CU',
    0x0020: u'Yamaha ADPCM',
    0x0021: u'Speech Compression Sonarc',
    0x0022: u'DSP Group TrueSpeech',
    0x0023: u'Echo Speech EchoSC1',
    0x0024: u'Audiofile AF36',
    0x0025: u'Audio Processing Technology APTX',
    0x0026: u'AudioFile AF10',
    0x0027: u'Prosody 1612',
    0x0028: u'LRC',
    0x0030: u'Dolby AC2',
    0x0031: u'Microsoft GSM 6.10',
    0x0032: u'MSNAudio',
    0x0033: u'Antex Electronics ADPCME',
    0x0034: u'Control Resources VQLPC',
    0x0035: u'DSP Solutions DigiREAL',
    0x0036: u'DSP Solutions DigiADPCM',
    0x0037: u'Control Resources CR10',
    0x0038: u'Natural MicroSystems VBXADPCM',
    0x0039: u'Crystal Semiconductor IMA ADPCM',
    0x003A: u'EchoSC3',
    0x003B: u'Rockwell ADPCM',
    0x003C: u'Rockwell Digit LK',
    0x003D: u'Xebec',
    0x0040: u'Antex Electronics G.721 ADPCM',
    0x0041: u'G.728 CELP',
    0x0042: u'MSG723',
    0x0050: u'Microsoft MPEG',
    0x0052: u'RT24',
    0x0053: u'PAC',
    0x0055: u'MPEG Layer 3',
    0x0059: u'Lucent G.723',
    0x0060: u'Cirrus',
    0x0061: u'ESPCM',
    0x0062: u'Voxware',
    0x0063: u'Canopus Atrac',
    0x0064: u'G.726 ADPCM',
    0x0065: u'G.722 ADPCM',
    0x0066: u'DSAT',
    0x0067: u'DSAT Display',
    0x0069: u'Voxware Byte Aligned',
    0x0070: u'Voxware AC8',
    0x0071: u'Voxware AC10',
    0x0072: u'Voxware AC16',
    0x0073: u'Voxware AC20',
    0x0074: u'Voxware MetaVoice',
    0x0075: u'Voxware MetaSound',
    0x0076: u'Voxware RT29HW',
    0x0077: u'Voxware VR12',
    0x0078: u'Voxware VR18',
    0x0079: u'Voxware TQ40',
    0x0080: u'Softsound',
    0x0081: u'Voxware TQ60',
    0x0082: u'MSRT24',
    0x0083: u'G.729A',
    0x0084: u'MVI MV12',
    0x0085: u'DF G.726',
    0x0086: u'DF GSM610',
    0x0088: u'ISIAudio',
    0x0089: u'Onlive',
    0x0091: u'SBC24',
    0x0092: u'Dolby AC3 SPDIF',
    0x0097: u'ZyXEL ADPCM',
    0x0098: u'Philips LPCBB',
    0x0099: u'Packed',
    0x0100: u'Rhetorex ADPCM',
    0x0101: u'IBM mu-law',
    0x0102: u'IBM A-law',
    0x0103: u'IBM AVC Adaptive Differential Pulse Code Modulation (ADPCM)',
    0x0111: u'Vivo G.723',
    0x0112: u'Vivo Siren',
    0x0123: u'Digital G.723',
    0x0140: u'Windows Media Video V8',
    0x0161: u'Windows Media Audio V7 / V8 / V9',
    0x0162: u'Windows Media Audio Professional V9',
    0x0163: u'Windows Media Audio Lossless V9',
    0x0200: u'Creative Labs ADPCM',
    0x0202: u'Creative Labs Fastspeech8',
    0x0203: u'Creative Labs Fastspeech10',
    0x0220: u'Quarterdeck',
    0x0300: u'Fujitsu FM Towns Snd',
    0x0400: u'BTV Digital',
    0x0680: u'VME VMPCM',
    0x1000: u'Olivetti GSM',
    0x1001: u'Olivetti ADPCM',
    0x1002: u'Olivetti CELP',
    0x1003: u'Olivetti SBC',
    0x1004: u'Olivetti OPR',
    0x1100: u'Lernout & Hauspie LH Codec',
    0x1400: u'Norris',
    0x1401: u'AT&T ISIAudio',
    0x1500: u'Soundspace Music Compression',
    0x2000: u'AC3',
    0x7A21: u'GSM-AMR (CBR, no SID)',
    0x7A22: u'GSM-AMR (VBR, including SID)',
    0xFFFF: u'Development codec'
}

video_fourcc_name = {
    '3IV1': u'3ivx v1',
    '3IV2': u'3ivx v2',
    'AASC': u'Autodesk Animator',
    'ABYR': u'Kensington ?ABYR?',
    'AEMI': u'Array VideoONE MPEG1-I Capture',
    'AFLC': u'Autodesk Animator FLC',
    'AFLI': u'Autodesk Animator FLI',
    'AMPG': u'Array VideoONE MPEG',
    'ANIM': u'Intel RDX (ANIM)',
    'AP41': u'AngelPotion Definitive',
    'ASV1': u'Asus Video v1',
    'ASV2': u'Asus Video v2',
    'ASVX': u'Asus Video 2.0 (audio)',
    'AUR2': u'Aura 2 Codec - YUV 4:2:2',
    'AURA': u'Aura 1 Codec - YUV 4:1:1',
    'BINK': u'RAD Game Tools Bink Video',
    'BT20': u'Conexant Prosumer Video',
    'BTCV': u'Conexant Composite Video Codec',
    'BW10': u'Data Translation Broadway MPEG Capture',
    'CC12': u'Intel YUV12',
    'CDVC': u'Canopus DV',
    'CFCC': u'Digital Processing Systems DPS Perception',
    'CGDI': u'Microsoft Office 97 Camcorder Video',
    'CHAM': u'Winnov Caviara Champagne',
    'CJPG': u'Creative WebCam JPEG',
    'CLJR': u'Cirrus Logic YUV 4 pixels',
    'CMYK': u'Common Data Format in Printing',
    'CPLA': u'Weitek 4:2:0 YUV Planar',
    'CRAM': u'Microsoft Video 1 (CRAM)',
    'CVID': u'Radius Cinepak',
    'CWLT': u'Microsoft Color WLT DIB',
    'CYUV': u'Creative Labs YUV',
    'CYUY': u'ATI YUV',
    'D261': u'H.261',
    'D263': u'H.263',
    'DIV3': u'DivX v3 MPEG-4 Low-Motion',
    'DIV4': u'DivX v3 MPEG-4 Fast-Motion',
    'DIV5': u'?DIV5?',
    'DIVX': u'DivX v4',
    'divx': u'DivX',
    'DMB1': u'Matrox Rainbow Runner hardware MJPEG',
    'DMB2': u'Paradigm MJPEG',
    'DSVD': u'?DSVD?',
    'DUCK': u'Duck True Motion 1.0',
    'DVAN': u'?DVAN?',
    'DVE2': u'InSoft DVE-2 Videoconferencing',
    'dvsd': u'DV',
    'DVSD': u'DV',
    'DVX1': u'DVX1000SP Video Decoder',
    'DVX2': u'DVX2000S Video Decoder',
    'DVX3': u'DVX3000S Video Decoder',
    'DX50': u'DivX v5',
    'DXT1': u'Microsoft DirectX Compressed Texture (DXT1)',
    'DXT2': u'Microsoft DirectX Compressed Texture (DXT2)',
    'DXT3': u'Microsoft DirectX Compressed Texture (DXT3)',
    'DXT4': u'Microsoft DirectX Compressed Texture (DXT4)',
    'DXT5': u'Microsoft DirectX Compressed Texture (DXT5)',
    'DXTC': u'Microsoft DirectX Compressed Texture (DXTC)',
    'EKQ0': u'Elsa ?EKQ0?',
    'ELK0': u'Elsa ?ELK0?',
    'ESCP': u'Eidos Escape',
    'ETV1': u'eTreppid Video ETV1',
    'ETV2': u'eTreppid Video ETV2',
    'ETVC': u'eTreppid Video ETVC',
    'FLJP': u'D-Vision Field Encoded Motion JPEG',
    'FRWA': u'SoftLab-Nsk Forward Motion JPEG w/ alpha channel',
    'FRWD': u'SoftLab-Nsk Forward Motion JPEG',
    'FVF1': u'Iterated Systems Fractal Video Frame',
    'GLZW': u'Motion LZW (gabest@freemail.hu)',
    'GPEG': u'Motion JPEG (gabest@freemail.hu)',
    'GWLT': u'Microsoft Greyscale WLT DIB',
    'H260': u'Intel ITU H.260 Videoconferencing',
    'H261': u'Intel ITU H.261 Videoconferencing',
    'H262': u'Intel ITU H.262 Videoconferencing',
    'H263': u'Intel ITU H.263 Videoconferencing',
    'H264': u'Intel ITU H.264 Videoconferencing',
    'H265': u'Intel ITU H.265 Videoconferencing',
    'H266': u'Intel ITU H.266 Videoconferencing',
    'H267': u'Intel ITU H.267 Videoconferencing',
    'H268': u'Intel ITU H.268 Videoconferencing',
    'H269': u'Intel ITU H.269 Videoconferencing',
    'HFYU': u'Huffman Lossless Codec',
    'HMCR': u'Rendition Motion Compensation Format (HMCR)',
    'HMRR': u'Rendition Motion Compensation Format (HMRR)',
    'i263': u'Intel ITU H.263 Videoconferencing (i263)',
    'I420': u'Intel Indeo 4',
    'IAN ': u'Intel RDX',
    'ICLB': u'InSoft CellB Videoconferencing',
    'IGOR': u'Power DVD',
    'IJPG': u'Intergraph JPEG',
    'ILVC': u'Intel Layered Video',
    'ILVR': u'ITU-T H.263+',
    'IPDV': u'I-O Data Device Giga AVI DV Codec',
    'IR21': u'Intel Indeo 2.1',
    'IRAW': u'Intel YUV Uncompressed',
    'IV30': u'Ligos Indeo 3.0',
    'IV31': u'Ligos Indeo 3.1',
    'IV32': u'Ligos Indeo 3.2',
    'IV33': u'Ligos Indeo 3.3',
    'IV34': u'Ligos Indeo 3.4',
    'IV35': u'Ligos Indeo 3.5',
    'IV36': u'Ligos Indeo 3.6',
    'IV37': u'Ligos Indeo 3.7',
    'IV38': u'Ligos Indeo 3.8',
    'IV39': u'Ligos Indeo 3.9',
    'IV40': u'Ligos Indeo Interactive 4.0',
    'IV41': u'Ligos Indeo Interactive 4.1',
    'IV42': u'Ligos Indeo Interactive 4.2',
    'IV43': u'Ligos Indeo Interactive 4.3',
    'IV44': u'Ligos Indeo Interactive 4.4',
    'IV45': u'Ligos Indeo Interactive 4.5',
    'IV46': u'Ligos Indeo Interactive 4.6',
    'IV47': u'Ligos Indeo Interactive 4.7',
    'IV48': u'Ligos Indeo Interactive 4.8',
    'IV49': u'Ligos Indeo Interactive 4.9',
    'IV50': u'Ligos Indeo Interactive 5.0',
    'JBYR': u'Kensington ?JBYR?',
    'JPEG': u'Still Image JPEG DIB',
    'JPGL': u'Webcam JPEG Light?',
    'KMVC': u'Karl Morton\'s Video Codec',
    'LEAD': u'LEAD Video Codec',
    'Ljpg': u'LEAD MJPEG Codec',
    'M261': u'Microsoft H.261',
    'M263': u'Microsoft H.263',
    'M4S2': u'Microsoft MPEG-4 (M4S2)',
    'm4s2': u'Microsoft MPEG-4 (m4s2)',
    'MC12': u'ATI Motion Compensation Format (MC12)',
    'MCAM': u'ATI Motion Compensation Format (MCAM)',
    'MJ2C': u'Morgan Multimedia Motion JPEG2000',
    'mJPG': u'IBM Motion JPEG w/ Huffman Tables',
    'MJPG': u'Motion JPEG DIB',
    'MP42': u'Microsoft MPEG-4 (low-motion)',
    'MP43': u'Microsoft MPEG-4 (fast-motion)',
    'MP4S': u'Microsoft MPEG-4 (MP4S)',
    'mp4s': u'Microsoft MPEG-4 (mp4s)',
    'MPEG': u'MPEG 1 Video I-Frame',
    'MPG4': u'Microsoft MPEG-4 Video High Speed Compressor',
    'MPGI': u'Sigma Designs MPEG',
    'MRCA': u'FAST Multimedia Mrcodec',
    'MRLE': u'Microsoft Run Length Encoding (RLE)',
    'MSVC': u'Microsoft Video 1',
    'MTX1': u'Matrox ?MTX1?',
    'MTX2': u'Matrox ?MTX2?',
    'MTX3': u'Matrox ?MTX3?',
    'MTX4': u'Matrox ?MTX4?',
    'MTX5': u'Matrox ?MTX5?',
    'MTX6': u'Matrox ?MTX6?',
    'MTX7': u'Matrox ?MTX7?',
    'MTX8': u'Matrox ?MTX8?',
    'MTX9': u'Matrox ?MTX9?',
    'MV12': u'?MV12?',
    'MWV1': u'Aware Motion Wavelets',
    'nAVI': u'?nAVI?',
    'NTN1': u'Nogatech Video Compression 1',
    'NVS0': u'nVidia GeForce Texture (NVS0)',
    'NVS1': u'nVidia GeForce Texture (NVS1)',
    'NVS2': u'nVidia GeForce Texture (NVS2)',
    'NVS3': u'nVidia GeForce Texture (NVS3)',
    'NVS4': u'nVidia GeForce Texture (NVS4)',
    'NVS5': u'nVidia GeForce Texture (NVS5)',
    'NVT0': u'nVidia GeForce Texture (NVT0)',
    'NVT1': u'nVidia GeForce Texture (NVT1)',
    'NVT2': u'nVidia GeForce Texture (NVT2)',
    'NVT3': u'nVidia GeForce Texture (NVT3)',
    'NVT4': u'nVidia GeForce Texture (NVT4)',
    'NVT5': u'nVidia GeForce Texture (NVT5)',
    'PDVC': u'I-O Data Device Digital Video Capture DV codec',
    'PGVV': u'Radius Video Vision',
    'PHMO': u'IBM Photomotion',
    'PIM1': u'Pegasus Imaging ?PIM1?',
    'PIM2': u'Pegasus Imaging ?PIM2?',
    'PIMJ': u'Pegasus Imaging Lossless JPEG',
    'PVEZ': u'Horizons Technology PowerEZ',
    'PVMM': u'PacketVideo Corporation MPEG-4',
    'PVW2': u'Pegasus Imaging Wavelet Compression',
    'QPEG': u'Q-Team QPEG 1.0',
    'qpeq': u'Q-Team QPEG 1.1',
    'RGBT': u'Computer Concepts 32-bit support',
    'RLE ': u'Microsoft Run Length Encoder',
    'RLE4': u'Run Length Encoded 4',
    'RLE8': u'Run Length Encoded 8',
    'RT21': u'Intel Real Time Video 2.1',
    'rv20': u'RealVideo G2',
    'rv30': u'RealVideo 8',
    'RVX ': u'Intel RDX (RVX )',
    's422': u'Tekram VideoCap C210 YUV 4:2:2',
    'SDCC': u'Sun Communication Digital Camera Codec',
    'SFMC': u'CrystalNet Surface Fitting Method',
    'SMSC': u'Radius SMSC',
    'SMSD': u'Radius SMSD',
    'smsv': u'WorldConnect Wavelet Video',
    'SPIG': u'Radius Spigot',
    'SPLC': u'Splash Studios ACM Audio Codec',
    'SQZ2': u'Microsoft VXTreme Video Codec V2',
    'STVA': u'ST CMOS Imager Data (Bayer)',
    'STVB': u'ST CMOS Imager Data (Nudged Bayer)',
    'STVC': u'ST CMOS Imager Data (Bunched)',
    'STVX': u'ST CMOS Imager Data (Extended CODEC Data Format)',
    'STVY': u'ST CMOS Imager Data (Extended CODEC Data Format with Correction Data)',
    'SV10': u'Sorenson Video R1',
    'SVQ1': u'Sorenson Video R3',
    'TLMS': u'TeraLogic Motion Intraframe Codec (TLMS)',
    'TLST': u'TeraLogic Motion Intraframe Codec (TLST)',
    'TM20': u'Duck TrueMotion 2.0',
    'TM2X': u'Duck TrueMotion 2X',
    'TMIC': u'TeraLogic Motion Intraframe Codec (TMIC)',
    'TMOT': u'Horizons Technology TrueMotion S',
    'tmot': u'Horizons TrueMotion Video Compression',
    'TR20': u'Duck TrueMotion RealTime 2.0',
    'TSCC': u'TechSmith Screen Capture Codec',
    'TV10': u'Tecomac Low-Bit Rate Codec',
    'TY0N': u'Trident ?TY0N?',
    'TY2C': u'Trident ?TY2C?',
    'TY2N': u'Trident ?TY2N?',
    'UCOD': u'eMajix.com ClearVideo',
    'ULTI': u'IBM Ultimotion',
    'UYVY': u'UYVY 4:2:2 byte ordering',
    'V261': u'Lucent VX2000S',
    'V422': u'24 bit YUV 4:2:2 Format',
    'V655': u'16 bit YUV 4:2:2 Format',
    'VCR1': u'ATI VCR 1.0',
    'VCR2': u'ATI VCR 2.0',
    'VCR3': u'ATI VCR 3.0',
    'VCR4': u'ATI VCR 4.0',
    'VCR5': u'ATI VCR 5.0',
    'VCR6': u'ATI VCR 6.0',
    'VCR7': u'ATI VCR 7.0',
    'VCR8': u'ATI VCR 8.0',
    'VCR9': u'ATI VCR 9.0',
    'VDCT': u'Video Maker Pro DIB',
    'VDOM': u'VDOnet VDOWave',
    'VDOW': u'VDOnet VDOLive (H.263)',
    'VDTZ': u'Darim Vison VideoTizer YUV',
    'VGPX': u'VGPixel Codec',
    'VIDS': u'Vitec Multimedia YUV 4:2:2 CCIR 601 for V422',
    'VIFP': u'?VIFP?',
    'VIVO': u'Vivo H.263 v2.00',
    'vivo': u'Vivo H.263',
    'VIXL': u'Miro Video XL',
    'VLV1': u'Videologic VLCAP.DRV',
    'VP30': u'On2 VP3.0',
    'VP31': u'On2 VP3.1',
    'VX1K': u'VX1000S Video Codec',
    'VX2K': u'VX2000S Video Codec',
    'VXSP': u'VX1000SP Video Codec',
    'WBVC': u'Winbond W9960',
    'WHAM': u'Microsoft Video 1 (WHAM)',
    'WINX': u'Winnov Software Compression',
    'WJPG': u'AverMedia Winbond JPEG',
    'WMV1': u'Windows Media Video V7',
    'WMV2': u'Windows Media Video V8',
    'WMV3': u'Windows Media Video V9',
    'WNV1': u'Winnov Hardware Compression',
    'x263': u'Xirlink H.263',
    'XLV0': u'NetXL Video Decoder',
    'XMPG': u'Xing MPEG (I-Frame only)',
    'XVID': u'XviD MPEG-4',
    'XXAN': u'?XXAN?',
    'Y211': u'YUV 2:1:1 Packed',
    'Y411': u'YUV 4:1:1 Packed',
    'Y41B': u'YUV 4:1:1 Planar',
    'Y41P': u'PC1 4:1:1',
    'Y41T': u'PC1 4:1:1 with transparency',
    'Y42B': u'YUV 4:2:2 Planar',
    'Y42T': u'PCI 4:2:2 with transparency',
    'Y8  ': u'Grayscale video',
    'YC12': u'Intel YUV12 Codec',
    'YUV8': u'Winnov Caviar YUV8',
    'YUV9': u'Intel YUV9',
    'YUY2': u'Uncompressed YUV 4:2:2',
    'YUYV': u'Canopus YUV',
    'YV12': u'YVU12 Planar',
    'YVU9': u'Intel YVU9 Planar',
    'YVYU': u'YVYU 4:2:2 byte ordering',
    'ZLIB': u'?ZLIB?',
    'ZPEG': u'Metheus Video Zipper'
}
