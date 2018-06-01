# derived from
#   http://s3.amazonaws.com/alexa-static/top-1m.csv.zip
# fetched 2018-05-22, see also
#   https://support.alexa.com/hc/en-us/sections/200063274-Top-Sites

alexa_top_1m_tlds_about = {
  'date': '2018-05-22',
  'source': 'http://s3.amazonaws.com/alexa-static/top-1m.csv.zip'
}

alexa_top_1m_tlds = {
  # zcat top-1m.csv.zip \
  #  | perl -ne 'chomp; s/.+\.//; $h{$_}++;
  #              END {
  #                for (sort { $h{$b} <=> $h{$a} } keys %h) {
  #                  print "\047", $_, "\047:", $h{$_}, ", ";
  #                }
  #              }' \
  #  | fold --width=70 -s | perl -lpe 's/^/  /; s/:/: /g; s/\s+$//'
  'com': 477059, 'ru': 50063, 'org': 47785, 'net': 42573, 'de': 29457,
  'br': 19476, 'uk': 16367, 'pl': 15077, 'ir': 13369, 'in': 12812,
  'au': 11239, 'fr': 9492, 'it': 9483, 'info': 9136, 'ua': 8126, 'ca': 8077,
  'cz': 7611, 'es': 7448, 'jp': 6807, 'nl': 6636, 'co': 6477, 'mx': 6384,
  'tw': 5700, 'hu': 5644, 'se': 5406, 'gr': 5273, 'io': 4975, 'eu': 4784,
  'ar': 4780, 'cn': 4340, 'ro': 3984, 'sk': 3980, 'me': 3882, 'ch': 3825,
  'tv': 3698, 'dk': 3667, 'za': 3663, 'id': 3548, 'kr': 3408, 'vn': 3285,
  'us': 3068, 'no': 3056, 'be': 3037, 'at': 2701, 'cl': 2637, 'edu': 2630,
  'tr': 2370, 'biz': 2217, 'xyz': 2094, 'sg': 2057, 'fi': 2052, 'pt': 1875,
  'club': 1804, 'hk': 1751, 'il': 1675, 'my': 1656, 'ie': 1605, 'az': 1547,
  'cc': 1489, 'pro': 1477, 'nz': 1446, 'online': 1429, 'by': 1399,
  'lt': 1262, 'th': 1259, 'kz': 1248, 'su': 1202, 'pk': 1180, 'si': 1144,
  'bg': 1142, 'hr': 1142, 'top': 1137, 'xn--p1ai': 1100, 'pe': 1016,
  'ng': 1014, 'site': 939, 'rs': 933, 'gov': 927, 'tk': 874, 'sa': 759,
  'pw': 728, 'ae': 719, 'ph': 676, 'lv': 657, 'uz': 614, 'to': 574,
  'mobi': 557, 'download': 545, 'win': 523, 'ee': 517, 'ws': 482, 'nu': 468,
  'bd': 455, 'eg': 448, 'xxx': 437, 've': 421, 'is': 420, 'ml': 409,
  'lk': 390, 'fm': 384, 'ga': 376, 'ge': 375, 'cat': 371, 'ma': 367,
  'am': 364, 'space': 363, 'stream': 339, 'news': 330, 'live': 323,
  'ec': 313, 'qa': 310, 'asia': 305, 'ba': 296, 'cf': 292, 'today': 281,
  'website': 280, 'tn': 259, 'life': 254, 'uy': 252, 'do': 246, 'blog': 246,
  'guru': 245, 'ly': 243, 'md': 241, 'bid': 237, 'gg': 233, 'name': 231,
  'mk': 228, 'tech': 223, 'dz': 219, 'lu': 219, 'shop': 216, 'ke': 208,
  'travel': 201, 'link': 199, 'la': 197, 'fun': 189, 'cr': 188, 'one': 176,
  'al': 172, 'ai': 169, 'store': 165, 'mn': 163, 'gq': 162, 'world': 157,
  'media': 156, 'bz': 149, 'kw': 147, 'im': 145, 'af': 144, 'jobs': 141,
  'cy': 141, 'tz': 140, 'network': 140, 'om': 139, 'video': 137, 'py': 135,
  'ug': 132, 'aero': 131, 'gt': 130, 'rocks': 126, 'cloud': 124, 'bo': 123,
  'mm': 120, 'kg': 119, 'trade': 118, 'np': 117, 'tj': 116, 'pa': 115,
  'sy': 113, 'zone': 113, 'click': 112, 'review': 110, 'cu': 108, 'sv': 106,
  'coop': 105, 'loan': 101, 'cm': 99, 'men': 98, 'jo': 98, 'vip': 95,
  'date': 93, 'li': 91, 'wiki': 89, 'eus': 88, 'porn': 86, 'moe': 85,
  'sd': 85, 'work': 85, 'global': 83, 'gdn': 82, 'center': 82, 'ninja': 81,
  'press': 80, 'lb': 80, 'st': 79, 'sh': 79, 'bh': 79, 'ag': 79, 'host': 78,
  'city': 74, 'ps': 73, 'science': 73, 'mz': 73, 'nyc': 73, 'tokyo': 71,
  'ac': 70, 'gh': 70, 'party': 70, 'design': 69, 'sexy': 68, 'plus': 68,
  'mu': 67, 'academy': 67, 'so': 66, 're': 65, 'iq': 65, 'int': 64, 'et': 64,
  'expert': 63, 'church': 62, 'tips': 61, 'zw': 59, 'pics': 59, 'cd': 56,
  'games': 55, 'mt': 54, 'bet': 54, 'ci': 54, 'rw': 54, 'hn': 54, 'ovh': 53,
  'ao': 52, 'vc': 51, 'cx': 51, 'red': 51, 'guide': 51, 'mg': 50, 'ni': 49,
  'tm': 49, 'mo': 48, 'tools': 47, 'sn': 47, 'cool': 47, 'studio': 46,
  'london': 45, 'education': 45, 'agency': 45, 'gratis': 45, 'tt': 44,
  'cash': 43, 'sc': 43, 'mil': 43, 'ms': 43, 'community': 43, 'email': 42,
  'land': 42, 'bank': 41, 'company': 41, 'bike': 41, 'social': 40,
  'audio': 40, 'kh': 39, 'digital': 39, 'ltd': 39, 'tf': 39, 'lol': 38,
  'pg': 38, 'help': 38, 'solutions': 37, 'pub': 37, 'market': 36, 'bw': 36,
  'team': 36, 'watch': 35, 'art': 35, 'berlin': 35, 'school': 34, 'chat': 34,
  'tl': 34, 'sx': 33, 'love': 33, 'gs': 32, 'exchange': 32, 'zm': 31,
  'services': 31, 'faith': 30, 'gl': 30, 'movie': 30, 'systems': 30,
  'xn--j1amh': 30, 'mw': 29, 'scot': 29, 'run': 29, 'money': 29, 'cafe': 28,
  'pf': 28, 'works': 28, 'pm': 28, 'kim': 28, 'pr': 28, 'blue': 28, 'bf': 28,
  'group': 28, 'bt': 28, 'as': 27, 'ink': 27, 'coffee': 26, 'xn--p1acf': 26,
  'sex': 25, 'events': 25, 'farm': 25, 'tc': 25, 'bn': 25, 'ht': 24,
  'paris': 24, 'nc': 24, 'na': 24, 'wtf': 23, 'bio': 22, 'careers': 22,
  'app': 22, 'ad': 22, 'rip': 22, 'reviews': 22, 'moscow': 22, 'gal': 22,
  'gold': 22, 'yt': 21, 'xn--80asehdb': 21, 'webcam': 21, 'fit': 20,
  'dating': 20, 'taipei': 20, 'photos': 20, 'mv': 20, 'gy': 20, 'wang': 20,
  'racing': 20, 'capital': 20, 'deals': 19, 'bi': 19, 'care': 19, 'game': 19,
  'fo': 19, 'bm': 19, 'training': 19, 'ooo': 19, 'lc': 19, 'amsterdam': 18,
  'pink': 18, 'ye': 18, 'jm': 18, 'film': 18, 'university': 18,
  'marketing': 18, 'house': 17, 'tube': 17, 'vg': 17, 'swiss': 17,
  'report': 17, 'menu': 17, 'support': 17, 'uno': 17, 'international': 16,
  'software': 16, 'gallery': 16, 'sale': 16, 'photography': 16,
  'istanbul': 16, 'cam': 15, 'camp': 15, 'mr': 15, 'dog': 15, 'codes': 15,
  'bzh': 15, 'foundation': 14, 'dj': 14, 'bj': 14, 'photo': 14, 'ne': 14,
  'fj': 14, 'technology': 14, 'onl': 13, 'museum': 13, 'fyi': 13,
  'tours': 13, 'sl': 13, 'cards': 13, 'ist': 13, 'institute': 13,
  'pizza': 12, 'express': 12, 'sz': 12, 'band': 12, 'xn--90ais': 12,
  'quebec': 12, 'va': 12, 'directory': 12, 'supply': 12, 'leclerc': 12,
  'direct': 12, 'fitness': 12, 'dance': 11, 'energy': 11, 'best': 11,
  'cricket': 11, 'dev': 11, 'college': 11, 'show': 11, 'rest': 11,
  'desi': 11, 'bar': 11, 'cv': 11, 'ky': 11, 'sm': 11, 'buzz': 10,
  'vegas': 10, 'kiwi': 10, 'ls': 10, 'africa': 10, 'brussels': 10,
  'hosting': 10, 'town': 10, 'xn--80adxhks': 10, 'how': 10, 'ngo': 9,
  'graphics': 9, 'wales': 9, 'earth': 9, 'wien': 9, 'beer': 9, 'business': 9,
  'je': 9, 'google': 9, 'wedding': 9, 'xn--d1acj3b': 9, 'partners': 9,
  'sr': 9, 'style': 9, 'fund': 9, 'gd': 9, 'wf': 9, 'clothing': 9, 'fish': 9,
  'coach': 9, 'vet': 8, 'vision': 8, 'mc': 8, 'pictures': 8, 'hamburg': 8,
  'adult': 8, 'green': 8, 'xn--80aswg': 8, 'ventures': 8, 'black': 8,
  'audi': 8, 'place': 8, 'garden': 8, 'ax': 8, 'sydney': 8, 'kitchen': 7,
  'fashion': 7, 'box': 7, 'lat': 7, 'tel': 7, 'nrw': 7, 'vin': 7, 'build': 7,
  'clinic': 7, 'schule': 7, 'krd': 7, 'golf': 7, 'shoes': 7, 'delivery': 7,
  'xin': 7, 'koeln': 7, 'restaurant': 7, 'tg': 7, 'accountant': 7,
  'parts': 7, 'football': 7, 'computer': 6, 'vote': 6, 'ski': 6,
  'management': 6, 'camera': 6, 'vu': 6, 'law': 6, 'pet': 6, 'xn--c1avg': 6,
  'finance': 6, 'cg': 6, 'enterprises': 6, 'gi': 6, 'eco': 6, 'gift': 6,
  'auction': 6, 'bnpparibas': 6, 'poker': 5, 'boutique': 5, 'sb': 5,
  'casa': 5, 'haus': 5, 'yokohama': 5, 'army': 5, 'engineering': 5,
  'bayern': 5, 'kaufen': 5, 'cheap': 5, 'wine': 5, 'gm': 5, 'bible': 5,
  'domains': 5, 'exposed': 5, 'legal': 5, 'promo': 5, 'toys': 4,
  'equipment': 4, 'horse': 4, 'yoga': 4, 'barclays': 4, 'apartments': 4,
  'archi': 4, 'soccer': 4, 'diet': 4, 'zip': 4, 'bot': 4, 'dental': 4,
  'gmbh': 4, 'barcelona': 4, 'abbott': 4, 'gent': 4, 'car': 4, 'solar': 4,
  'builders': 4, 'frl': 4, 'recipes': 4, 'hockey': 4, 'tattoo': 4,
  'canon': 4, 'td': 4, 'saarland': 4, 'mp': 4, 'ki': 4, 'melbourne': 4,
  'creditcard': 4, 'mortgage': 4, 'health': 4, 'bradesco': 4,
  'vlaanderen': 4, 'okinawa': 4, 'xn--3e0b707e': 4, 'post': 4,
  'property': 4, 'realtor': 4, 'tienda': 4, 'rio': 4, 'basketball': 3,
  'man': 3, 'futbol': 3, 'doctor': 3, 'moda': 3, 'bb': 3, 'casino': 3,
  'organic': 3, 'sap': 3, 'estate': 3, 'gives': 3, 'holiday': 3, 'aq': 3,
  'repair': 3, 'vi': 3, 'gn': 3, 'monash': 3, 'kp': 3, 'auto': 3, 'soy': 3,
  'xn--90ae': 3, 'sandvik': 3, 'goog': 3, 'pn': 3, 'gp': 3, 'gf': 3,
  'corsica': 3, 'barclaycard': 3, 'contractors': 3, 'fail': 3, 'tax': 3,
  'discount': 3, 'nagoya': 3, 'rentals': 3, 'sbi': 3, 'ruhr': 3, 'taxi': 3,
  'cern': 3, 'bs': 3, 'mba': 3, 'diamonds': 3, 'miami': 3, 'investments': 3,
  'tirol': 3, 'family': 3, 'singles': 3, 'ren': 3, 'cab': 3, 'dm': 3,
  'pictet': 2, 'associates': 2, 'nf': 2, 'office': 2, 'sky': 2, 'cba': 2,
  'xn--mgbab2bd': 2, 'shopping': 2, 'vanguard': 2, 'lgbt': 2, 'sony': 2,
  'glass': 2, 'cymru': 2, 'flowers': 2, 'holdings': 2, 'seat': 2, 'med': 2,
  'consulting': 2, 'jcb': 2, 'fans': 2, 'ads': 2, 'irish': 2, 'sncf': 2,
  'study': 2, 'luxury': 2, 'yandex': 2, 'xn--fiqs8s': 2, 'pharmacy': 2,
  'immo': 2, 'rent': 2, 'orange': 2, 'lr': 2, 'radio': 2, 'cw': 2,
  'properties': 2, 'observer': 2, 'ismaili': 2, 'kyoto': 2,
  'productions': 2, 'theater': 2, 'markets': 2, 'lighting': 2,
  'industries': 2, 'coupons': 2, 'tatar': 2, 'forsale': 2, 'hm': 2, 'inc': 2,
  'telefonica': 2, 'reisen': 2, 'dhl': 2, 'weber': 2, 'aw': 2, 'juegos': 2,
  'mobile': 2, 'hot': 2, 'courses': 2, 'nico': 2, 'nr': 2, 'christmas': 1,
  'attorney': 1, 'yahoo': 1, 'srl': 1, 'maison': 1, 'sarl': 1, 'actor': 1,
  'docs': 1, 'salon': 1, 'viajes': 1, 'natura': 1, 'schmidt': 1,
  'chintai': 1, 'kred': 1, 'supplies': 1, 'ong': 1, 'lawyer': 1,
  'immobilien': 1, 'komatsu': 1, 'xn--wgbl6a': 1, 'fox': 1, 'fk': 1,
  'madrid': 1, 'hiv': 1, 'plumbing': 1, 'xn--e1a4c': 1, 'bingo': 1, 'gw': 1,
  'security': 1, 'aws': 1, 'loans': 1, 'weather': 1, 'trading': 1,
  'cruises': 1, 'hitachi': 1, 'alsace': 1, 'durban': 1, 'financial': 1,
  'george': 1, 'shiksha': 1, 'globo': 1, 'xn--54b7fta0cc': 1, 'physio': 1,
  'teva': 1, 'country': 1, 'voto': 1, 'surgery': 1, 'baidu': 1, 'gop': 1,
  'mattel': 1, 'mom': 1, 'jll': 1, 'chase': 1, 'cars': 1, 'cooking': 1,
  'er': 1, 'prime': 1, 'gifts': 1, 'now': 1, 'xn--h2brj9c': 1, 'jewelry': 1,
  'axa': 1, 'uol': 1, 'java': 1, 'drive': 1, 'surf': 1, 'lease': 1,
  'gmail': 1, 'florist': 1, 'hiphop': 1, 'accountants': 1, 'credit': 1,
  'weir': 1, 'bom': 1, 'mopar': 1, 'meet': 1, 'career': 1, 'foo': 1,
  'degree': 1, 'youtube': 1, 'tab': 1, 'anz': 1, 'insure': 1, 'neustar': 1,
  'ck': 1, 'comcast': 1, 'crs': 1, 'claims': 1, 'guitars': 1, 'limited': 1,
  'flights': 1, 'reise': 1, 'saxo': 1, 'osaka': 1, 'brother': 1, 'toyota': 1,
  'here': 1, 'healthcare': 1, 'honda': 1, 'vacations': 1, 'forex': 1,
  'play': 1, 'new': 1,
}
