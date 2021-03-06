dictionary_tag         = "Kulkarni et al. 2019"

reference              = "Kulkarni, Worseck, Hennawi; MNRAS 488, 1035 (2019)"
 
url                    = "https://academic.oup.com/mnras/article/488/1/1035/5510422"

description            = \
"""
Results from a sample of >80000 QSOs homogeneised to the same cosmologies, intrinsic AGN spectra and
magnitude system. The 3rd dimension of this dataset (labeled "data source" contains a string indicating
the original source of the QSOs sample. In this file, two additional arrays are stored - left and right - 
containing the magnitude range spanned by a single datapoint (i.e. the magnitude bin used to compute 
the constraint on the QLF).
"""

data_structure         = "points"

extracted              = False

ndim                   = 3

dimensions_descriptors = ["redshift", "M_1450", "data source"]

axes = [[0.31, -24.6, 'Richards et al. 2006'], [0.31, -24.0, 'Richards et al. 2006'],
        [0.31, -23.4, 'Richards et al. 2006'], [0.31, -22.8, 'Richards et al. 2006'],
        [0.31, -22.2, 'Richards et al. 2006'], [0.31, -21.6, 'Richards et al. 2006'],
        [0.31, -21.0, 'Richards et al. 2006'], [0.31, -20.4, 'Richards et al. 2006'],
        [0.5, -23.4, 'Croom et al. 2009'], [0.5, -22.8, 'Croom et al. 2009'],
        [0.5, -22.2, 'Croom et al. 2009'], [0.5, -21.6, 'Croom et al. 2009'],
        [0.5, -21.0, 'Croom et al. 2009'], [0.5, -20.4, 'Croom et al. 2009'],
        [0.5, -19.8, 'Croom et al. 2009'], [0.5, -19.2, 'Croom et al. 2009'],
        [0.5, -25.2, 'Richards et al. 2006'], [0.5, -24.6, 'Richards et al. 2006'],
        [0.5, -24.0, 'Richards et al. 2006'], [0.5, -23.4, 'Richards et al. 2006'],
        [0.5, -22.8, 'Richards et al. 2006'], [0.5, -22.2, 'Richards et al. 2006'],
        [0.5, -21.6, 'Richards et al. 2006'], [0.72, -24.0, 'Croom et al. 2009'],
        [0.72, -23.4, 'Croom et al. 2009'], [0.72, -22.8, 'Croom et al. 2009'],
        [0.72, -22.2, 'Croom et al. 2009'], [0.72, -21.6, 'Croom et al. 2009'],
        [0.72, -21.0, 'Croom et al. 2009'], [0.72, -26.4, 'Richards et al. 2006'],
        [0.72, -25.8, 'Richards et al. 2006'], [0.72, -25.2, 'Richards et al. 2006'],
        [0.72, -24.6, 'Richards et al. 2006'], [0.72, -24.0, 'Richards et al. 2006'],
        [0.72, -23.4, 'Richards et al. 2006'], [0.91, -24.6, 'Croom et al. 2009'],
        [0.91, -24.0, 'Croom et al. 2009'], [0.91, -23.4, 'Croom et al. 2009'],
        [0.91, -22.8, 'Croom et al. 2009'], [0.91, -22.2, 'Croom et al. 2009'],
        [0.91, -27.6, 'Richards et al. 2006'], [0.91, -27.0, 'Richards et al. 2006'],
        [0.91, -26.4, 'Richards et al. 2006'], [0.91, -25.8, 'Richards et al. 2006'],
        [0.91, -25.2, 'Richards et al. 2006'], [0.91, -24.6, 'Richards et al. 2006'],
        [0.91, -24.0, 'Richards et al. 2006'], [1.1, -25.2, 'Croom et al. 2009'],
        [1.1, -24.6, 'Croom et al. 2009'], [1.1, -24.0, 'Croom et al. 2009'],
        [1.1, -23.4, 'Croom et al. 2009'], [1.1, -22.8, 'Croom et al. 2009'],
        [1.1, -22.2, 'Croom et al. 2009'], [1.1, -28.2, 'Richards et al. 2006'],
        [1.1, -27.6, 'Richards et al. 2006'], [1.1, -27.0, 'Richards et al. 2006'],
        [1.1, -26.4, 'Richards et al. 2006'], [1.1, -25.8, 'Richards et al. 2006'],
        [1.1, -25.2, 'Richards et al. 2006'], [1.1, -24.6, 'Richards et al. 2006'],
        [1.1, -24.0, 'Richards et al. 2006'], [1.3, -25.8, 'Croom et al. 2009'],
        [1.3, -25.2, 'Croom et al. 2009'], [1.3, -24.6, 'Croom et al. 2009'],
        [1.3, -24.0, 'Croom et al. 2009'], [1.3, -23.4, 'Croom et al. 2009'],
        [1.3, -22.8, 'Croom et al. 2009'], [1.3, -28.2, 'Richards et al. 2006'],
        [1.3, -27.6, 'Richards et al. 2006'], [1.3, -27.0, 'Richards et al. 2006'],
        [1.3, -26.4, 'Richards et al. 2006'], [1.3, -25.8, 'Richards et al. 2006'],
        [1.3, -25.2, 'Richards et al. 2006'], [1.3, -24.6, 'Richards et al. 2006'],
        [1.5, -25.8, 'Croom et al. 2009'], [1.5, -25.2, 'Croom et al. 2009'],
        [1.5, -24.6, 'Croom et al. 2009'], [1.5, -24.0, 'Croom et al. 2009'],
        [1.5, -23.4, 'Croom et al. 2009'], [1.5, -22.8, 'Croom et al. 2009'],
        [1.5, -28.2, 'Richards et al. 2006'], [1.5, -27.6, 'Richards et al. 2006'],
        [1.5, -27.0, 'Richards et al. 2006'], [1.5, -26.4, 'Richards et al. 2006'],
        [1.5, -25.8, 'Richards et al. 2006'], [1.5, -25.2, 'Richards et al. 2006'],
        [1.5, -24.6, 'Richards et al. 2006'], [1.71, -26.4, 'Croom et al. 2009'],
        [1.71, -25.8, 'Croom et al. 2009'], [1.71, -25.2, 'Croom et al. 2009'],
        [1.71, -24.6, 'Croom et al. 2009'], [1.71, -24.0, 'Croom et al. 2009'],
        [1.71, -23.4, 'Croom et al. 2009'], [1.71, -22.8, 'Croom et al. 2009'],
        [1.71, -28.2, 'Richards et al. 2006'], [1.71, -27.6, 'Richards et al. 2006'],
        [1.71, -27.0, 'Richards et al. 2006'], [1.71, -26.4, 'Richards et al. 2006'],
        [1.71, -25.8, 'Richards et al. 2006'], [1.71, -25.2, 'Richards et al. 2006'],
        [1.98, -27.0, 'Croom et al. 2009'], [1.98, -26.4, 'Croom et al. 2009'],
        [1.98, -25.8, 'Croom et al. 2009'], [1.98, -25.2, 'Croom et al. 2009'],
        [1.98, -24.6, 'Croom et al. 2009'], [1.98, -24.0, 'Croom et al. 2009'],
        [1.98, -23.4, 'Croom et al. 2009'], [1.98, -28.8, 'Richards et al. 2006'],
        [1.98, -28.2, 'Richards et al. 2006'], [1.98, -27.6, 'Richards et al. 2006'],
        [1.98, -27.0, 'Richards et al. 2006'], [1.98, -26.4, 'Richards et al. 2006'],
        [1.98, -25.8, 'Richards et al. 2006'], [1.98, -25.2, 'Richards et al. 2006'],
        [2.3, -27.0, 'Ross et al. 2013'], [2.3, -26.4, 'Ross et al. 2013'],
        [2.3, -25.8, 'Ross et al. 2013'], [2.3, -25.2, 'Ross et al. 2013'],
        [2.3, -24.6, 'Ross et al. 2013'], [2.3, -24.0, 'Ross et al. 2013'],
        [2.3, -23.4, 'Ross et al. 2013'], [2.3, -22.8, 'Ross et al. 2013'],
        [2.45, -27.0, 'Ross et al. 2013'], [2.45, -26.4, 'Ross et al. 2013'],
        [2.45, -25.8, 'Ross et al. 2013'], [2.45, -25.2, 'Ross et al. 2013'],
        [2.45, -24.6, 'Ross et al. 2013'], [2.45, -24.0, 'Ross et al. 2013'],
        [2.45, -23.4, 'Ross et al. 2013'], [2.45, -22.8, 'Ross et al. 2013'],
        [2.55, -27.0, 'Ross et al. 2013'], [2.55, -26.4, 'Ross et al. 2013'],
        [2.55, -25.8, 'Ross et al. 2013'], [2.55, -25.2, 'Ross et al. 2013'],
        [2.55, -24.6, 'Ross et al. 2013'], [2.55, -24.0, 'Ross et al. 2013'],
        [2.55, -23.4, 'Ross et al. 2013'], [2.55, -22.8, 'Ross et al. 2013'],
        [2.65, -27.0, 'Ross et al. 2013'], [2.65, -26.4, 'Ross et al. 2013'],
        [2.65, -25.8, 'Ross et al. 2013'], [2.65, -25.2, 'Ross et al. 2013'],
        [2.65, -24.6, 'Ross et al. 2013'], [2.65, -24.0, 'Ross et al. 2013'],
        [2.65, -23.4, 'Ross et al. 2013'], [2.75, -27.0, 'Ross et al. 2013'],
        [2.75, -26.4, 'Ross et al. 2013'], [2.75, -25.8, 'Ross et al. 2013'],
        [2.75, -25.2, 'Ross et al. 2013'], [2.75, -24.6, 'Ross et al. 2013'],
        [2.75, -24.0, 'Ross et al. 2013'], [2.75, -23.4, 'Ross et al. 2013'],
        [2.85, -27.0, 'Ross et al. 2013'], [2.85, -26.4, 'Ross et al. 2013'],
        [2.85, -25.8, 'Ross et al. 2013'], [2.85, -25.2, 'Ross et al. 2013'],
        [2.85, -24.6, 'Ross et al. 2013'], [2.85, -24.0, 'Ross et al. 2013'],
        [2.85, -23.4, 'Ross et al. 2013'], [2.95, -27.6, 'Ross et al. 2013'],
        [2.95, -27.0, 'Ross et al. 2013'], [2.95, -26.4, 'Ross et al. 2013'],
        [2.95, -25.8, 'Ross et al. 2013'], [2.95, -25.2, 'Ross et al. 2013'],
        [2.95, -24.6, 'Ross et al. 2013'], [2.95, -24.0, 'Ross et al. 2013'],
        [2.95, -23.4, 'Ross et al. 2013'], [3.05, -27.6, 'Ross et al. 2013'],
        [3.05, -27.0, 'Ross et al. 2013'], [3.05, -26.4, 'Ross et al. 2013'],
        [3.05, -25.8, 'Ross et al. 2013'], [3.05, -25.2, 'Ross et al. 2013'],
        [3.05, -24.6, 'Ross et al. 2013'], [3.05, -24.0, 'Ross et al. 2013'],
        [3.05, -23.4, 'Ross et al. 2013'], [3.15, -27.6, 'Ross et al. 2013'],
        [3.15, -27.0, 'Ross et al. 2013'], [3.15, -26.4, 'Ross et al. 2013'],
        [3.15, -25.8, 'Ross et al. 2013'], [3.15, -25.2, 'Ross et al. 2013'],
        [3.15, -24.6, 'Ross et al. 2013'], [3.15, -24.0, 'Ross et al. 2013'],
        [3.15, -23.4, 'Ross et al. 2013'], [3.25, -27.6, 'Ross et al. 2013'],
        [3.25, -27.0, 'Ross et al. 2013'], [3.25, -26.4, 'Ross et al. 2013'],
        [3.25, -25.8, 'Ross et al. 2013'], [3.25, -25.2, 'Ross et al. 2013'],
        [3.25, -24.6, 'Ross et al. 2013'], [3.25, -24.0, 'Ross et al. 2013'],
        [3.25, -23.4, 'Ross et al. 2013'], [3.34, -27.6, 'Ross et al. 2013'],
        [3.34, -27.0, 'Ross et al. 2013'], [3.34, -26.4, 'Ross et al. 2013'],
        [3.34, -25.8, 'Ross et al. 2013'], [3.34, -25.2, 'Ross et al. 2013'],
        [3.34, -24.6, 'Ross et al. 2013'], [3.34, -24.0, 'Ross et al. 2013'],
        [3.34, -23.4, 'Ross et al. 2013'], [3.44, -27.6, 'Ross et al. 2013'],
        [3.44, -27.0, 'Ross et al. 2013'], [3.44, -26.4, 'Ross et al. 2013'],
        [3.44, -25.8, 'Ross et al. 2013'], [3.44, -25.2, 'Ross et al. 2013'],
        [3.44, -24.6, 'Ross et al. 2013'], [3.44, -24.0, 'Ross et al. 2013'],
        [3.88, -28.8, 'Richards et al. 2006'], [3.88, -28.2, 'Richards et al. 2006'],
        [3.88, -27.6, 'Richards et al. 2006'], [3.88, -27.0, 'Richards et al. 2006'],
        [3.88, -26.4, 'Richards et al. 2006'], [3.88, -25.5, 'Glikman et al. 2011'],
        [3.88, -24.5, 'Glikman et al. 2011'], [3.88, -23.5, 'Glikman et al. 2011'],
        [3.88, -22.5, 'Glikman et al. 2011'], [4.35, -28.8, 'Richards et al. 2006'],
        [4.35, -28.2, 'Richards et al. 2006'], [4.35, -27.6, 'Richards et al. 2006'],
        [4.35, -27.0, 'Richards et al. 2006'], [4.35, -26.4, 'Richards et al. 2006'],
        [4.35, -25.5, 'Glikman et al. 2011'], [4.35, -24.5, 'Glikman et al. 2011'],
        [4.35, -23.5, 'Glikman et al. 2011'], [4.92, -28.8, 'Yang et al. 2016'],
        [4.92, -28.2, 'Yang et al. 2016'], [4.92, -27.6, 'Yang et al. 2016'],
        [4.92, -27.0, 'Yang et al. 2016'], [4.92, -26.4, 'McGreer et al. 2013'],
        [4.92, -25.8, 'McGreer et al. 2013'], [4.92, -25.2, 'McGreer et al. 2013'],
        [4.92, -24.6, 'McGreer et al. 2013'], [4.92, -24.0, 'McGreer et al. 2013'],
        [4.92, -25.5, 'Glikman et al. 2011'], [4.92, -24.5, 'Glikman et al. 2011'],
        [6.0, -30.0, 'Jiang et al. 2016'], [6.0, -28.2, 'Jiang et al. 2016'],
        [6.0, -26.4, 'Jiang et al. 2016'], [6.0, -24.6, 'Jiang et al. 2016'],
        [6.0, -23.4, 'Kashikawa et al. 2015'], [6.0, -22.8, 'Kashikawa et al. 2015'],
        [6.0, -26.4, 'Willott et al. 2010'], [6.0, -24.6, 'Willott et al. 2010'],
        [6.0, -22.8, 'Willott et al. 2010']
       ]

values = [ -8.33632132,  -7.59157013,  -7.14239961,  -6.76083547,
           -6.49363912,  -6.07966811,  -5.96629613,  -5.8002448 ,
           -6.54965332,  -6.4632394 ,  -6.00893812,  -5.69177645,
           -5.82855257,  -5.53626444,  -5.60611388,  -5.73001095,
           -8.25766333,  -7.56542671,  -7.09057331,  -6.71343049,
           -6.37902963,  -6.16863276,  -6.11661255,  -6.95419061,
           -6.28171061,  -6.04353888,  -5.82421277,  -5.58266587,
           -5.45968238,  -8.8595374 ,  -8.42854464,  -7.59215721,
           -7.10228436,  -6.7084171 ,  -6.40771202,  -6.75967407,
           -6.29435359,  -6.16153408,  -5.8747809 ,  -5.61612142,
           -9.51098965,  -9.40331963,  -8.40331963,  -7.75495962,
           -7.22434268,  -6.74073273,  -6.39909075,  -6.90637031,
           -6.48856087,  -6.23550534,  -5.85895652,  -5.71795965,
           -5.56861732,  -9.25978838,  -9.48570675,  -8.74534406,
           -8.04637406,  -7.43455423,  -6.88268854,  -6.45458067,
           -6.31173224,  -7.15923985,  -6.86215229,  -6.37250615,
           -6.0381896 ,  -5.81700915,  -5.59412662,  -9.78539308,
           -9.06336448,  -8.25045113,  -7.76963373,  -7.12467801,
           -6.67481691,  -6.28319444,  -7.05721148,  -6.53323608,
           -6.16881812,  -5.92964378,  -5.65377982,  -5.55110873,
           -9.87816585,  -9.03306781,  -8.12997783,  -7.47333214,
           -6.9361578 ,  -6.46573427,  -6.27929938,  -7.08782787,
           -6.74955897,  -6.32716749,  -6.11571019,  -5.84070847,
           -5.65577288,  -5.5482019 ,  -9.60139105,  -8.55999836,
           -7.95793837,  -7.30692482,  -6.76153563,  -6.34369128,
           -7.3817265 ,  -7.05399979,  -6.61039343,  -6.30140175,
           -5.97771456,  -5.76422048,  -5.66206812,  -9.74604392,
           -9.10924028,  -8.30408711,  -7.72901966,  -7.12343854,
           -6.65741966,  -6.47095243,  -7.39988964,  -7.07416207,
           -6.63119041,  -6.29717527,  -6.03517583,  -5.80685075,
           -5.70317539,  -5.52101758,  -7.52645177,  -7.07656759,
           -6.64703461,  -6.34068314,  -6.14001398,  -5.95212107,
           -5.86710318,  -5.53248345,  -7.60021526,  -7.18009519,
           -6.7180229 ,  -6.38300597,  -6.14487238,  -5.94624505,
           -5.93073763,  -5.42275783,  -7.40629518,  -7.13876734,
           -6.62584053,  -6.31255843,  -6.07493594,  -5.99505789,
           -6.03677135,  -7.4597101 ,  -6.9281122 ,  -6.50948393,
           -6.22681606,  -6.16501122,  -6.00698377,  -6.03705861,
           -7.29044577,  -6.83010997,  -6.56782947,  -6.28074545,
           -6.18578368,  -6.03583638,  -6.00123386,  -7.56306621,
           -7.6418143 ,  -6.87811058,  -6.6407906 ,  -6.39470786,
           -6.18729968,  -6.04086217,  -5.8957323 ,  -8.18161283,
           -7.54430379,  -7.03914801,  -6.63879921,  -6.39234828,
           -6.28167135,  -6.11098559,  -5.94991638,  -8.18120417,
           -7.37436377,  -7.11709364,  -6.73978322,  -6.47473248,
           -6.32404474,  -6.15596168,  -5.55864655,  -7.7191376 ,
           -7.56816429,  -7.0523076 ,  -6.82865428,  -6.55960207,
           -6.42202974,  -6.19570657,  -5.73692431,  -7.88914627,
           -7.52028436,  -7.13128479,  -6.80239227,  -6.61317503,
           -6.3476817 ,  -6.09850119,  -5.2984278 ,  -7.5932653 ,
           -7.48275601,  -6.88344636,  -6.71706803,  -6.70881   ,
           -6.59018423,  -6.40664312,  -9.89133243,  -9.49329992,
           -8.56897637,  -7.93832088,  -7.59698836,  -6.87903202,
           -6.25339706,  -6.32838202,  -6.14027988, -10.04707995,
           -9.4449889 ,  -8.81650057,  -8.32651832,  -7.89686372,
           -6.51234884,  -7.17871227,  -6.31398787, -10.25114737,
           -9.65694927,  -9.07376445,  -8.67683754,  -8.06379095,
           -8.37737978,  -7.43164636,  -7.24627514,  -7.23999146,
           -6.93759864,  -6.65998944, -10.2873256 , -10.06051372,
           -9.1753812 ,  -8.16246583,  -7.10039188,  -6.86487205,
           -9.13938293,  -8.10605748,  -7.37597285
         ]

err_up = [0.29506734, 0.10101816, 0.05395614, 0.03400696, 0.02270855,
          0.0154825 , 0.01195104, 0.0167905 , 0.18712898, 0.09056166,
          0.06534233, 0.04887534, 0.05073323, 0.04720468, 0.06676318,
          0.14659368, 0.13397037, 0.05739085, 0.03250572, 0.02084564,
          0.01436008, 0.01120544, 0.01435237, 0.16336694, 0.06466438,
          0.05174371, 0.04226697, 0.03295359, 0.03182522, 0.22440214,
          0.12873107, 0.04643016, 0.02585821, 0.0166327 , 0.01117245,
          0.10926223, 0.05559563, 0.0480186 , 0.03788746, 0.0298065 ,
          0.51845163, 0.3652876 , 0.10630174, 0.04829924, 0.02568196,
          0.01493304, 0.00960443, 0.12873107, 0.06274802, 0.04643016,
          0.0349472 , 0.02896105, 0.02391729, 0.51845163, 0.3652876 ,
          0.14659368, 0.06214536, 0.0298746 , 0.01555061, 0.00956977,
          0.0092592 , 0.29506734, 0.08718173, 0.04977876, 0.03950395,
          0.03080421, 0.02367393, 0.51845163, 0.20337931, 0.07450112,
          0.04170539, 0.01943129, 0.0114214 , 0.00740439, 0.11981378,
          0.05647227, 0.0420773 , 0.03304537, 0.0239882 , 0.02330595,
          0.51845163, 0.18712898, 0.06155937, 0.02806876, 0.01492437,
          0.00858964, 0.00852223, 0.20337931, 0.07075311, 0.04643016,
          0.03845238, 0.0313417 , 0.02270855, 0.02264828, 0.3652876 ,
          0.10101816, 0.04858477, 0.02241187, 0.0118064 , 0.00726238,
          0.51845163, 0.0755324 , 0.04226697, 0.03142077, 0.02405974,
          0.01851123, 0.01688986, 0.29506734, 0.13397037, 0.05009101,
          0.0252565 , 0.01241393, 0.00721157, 0.00778992, 0.09435357,
          0.03286255, 0.01906155, 0.01311959, 0.01020154, 0.00950832,
          0.01024917, 0.01669287, 0.10630174, 0.04265401, 0.02563846,
          0.01847839, 0.01611878, 0.01543439, 0.01734611, 0.03451992,
          0.09864726, 0.04829924, 0.02801214, 0.02054725, 0.01755322,
          0.01722529, 0.02110845, 0.05602891, 0.08011802, 0.05209393,
          0.03015172, 0.02427822, 0.02120649, 0.02063771, 0.02684637,
          0.1124748 , 0.05936789, 0.04014438, 0.03250572, 0.03015172,
          0.02461729, 0.03390706, 0.10356236, 0.05395614, 0.04014438,
          0.03286255, 0.0296049 , 0.02636207, 0.03845238, 0.3652876 ,
          0.13397037, 0.05040911, 0.03816683, 0.03058208, 0.02679675,
          0.02812572, 0.0411653 , 0.51845163, 0.10356236, 0.05435264,
          0.03390706, 0.02660095, 0.02631506, 0.03008173, 0.05692611,
          0.3652876 , 0.07772659, 0.05517205, 0.03620814, 0.02699689,
          0.0266495 , 0.03451992, 0.06274802, 0.17410131, 0.09864726,
          0.05174371, 0.03982036, 0.03001221, 0.0313417 , 0.04047632,
          0.09643104, 0.20337931, 0.10356236, 0.06274802, 0.04521865,
          0.03830882, 0.03874435, 0.06534233, 0.29506734, 0.20337931,
          0.15433113, 0.0725564 , 0.06676318, 0.08011802, 0.13397037,
          0.29506734, 0.3652876 , 0.22440214, 0.07163815, 0.03361248,
          0.02255876, 0.51845163, 0.25301999, 0.29506734, 0.3652876 ,
          0.3652876 , 0.17410131, 0.08011802, 0.04431389, 0.02660095,
          0.22440214, 0.51845163, 0.22440214, 0.3652876 , 0.17410131,
          0.08414484, 0.06043448, 0.04668415, 0.1124748 , 0.12404183,
          0.09643104, 0.17410131, 0.51845163, 0.51845163, 0.51845163,
          0.15433113, 0.08882492, 0.17410131, 0.51845163, 0.51845163,
          0.29506734, 0.13397037, 0.51845163
         ]

err_down = [0.34125893, 0.10323592, 0.05432308, 0.03410278, 0.02273783,
            0.01549195, 0.01195542, 0.01680251, 0.19982028, 0.09218613,
            0.06597991, 0.04915089, 0.05104025, 0.04745379, 0.06744147,
            0.1529649 , 0.13890982, 0.05782944, 0.03258969, 0.02086839,
            0.01436764, 0.01120906, 0.01435991, 0.17201799, 0.0652831 ,
            0.05206877, 0.04244766, 0.03304098, 0.03190415, 0.24560444,
            0.13314327, 0.04666758, 0.02590113, 0.01664438, 0.01117604,
            0.11203404, 0.05599574, 0.04828037, 0.03801884, 0.02987163,
            0.76257244, 0.450883  , 0.10886547, 0.04856548, 0.02572403,
            0.01494153, 0.00960672, 0.13314327, 0.06331539, 0.04666758,
            0.03505097, 0.02902092, 0.02395141, 0.76257244, 0.450883  ,
            0.1529649 , 0.06269716, 0.02994017, 0.01556018, 0.00957203,
            0.00926125, 0.34125893, 0.08863906, 0.05006934, 0.03965234,
            0.03087594, 0.02370704, 0.76257244, 0.21943445, 0.07543051,
            0.04187918, 0.01944979, 0.01142523, 0.00740545, 0.12341418,
            0.05689089, 0.04225564, 0.03313348, 0.02402262, 0.02333757,
            0.76257244, 0.19982028, 0.06209631, 0.02812337, 0.01493284,
            0.00859128, 0.00852383, 0.21943445, 0.07155453, 0.04666758,
            0.03858955, 0.03141716, 0.02273783, 0.02267733, 0.450883  ,
            0.10323592, 0.0488556 , 0.02244005, 0.01181063, 0.00726338,
            0.76257244, 0.07649916, 0.04244766, 0.03149679, 0.02409446,
            0.01852726, 0.01690208, 0.34125893, 0.13890982, 0.0503869 ,
            0.02529655, 0.01241884, 0.00721254, 0.00779115, 0.09617959,
            0.03294924, 0.01907903, 0.01312537, 0.01020428, 0.00951054,
            0.01025194, 0.01670467, 0.10886547, 0.04283955, 0.02568031,
            0.01849433, 0.01612942, 0.01544375, 0.01735934, 0.03462002,
            0.10072007, 0.04856548, 0.02806642, 0.02056906, 0.01756692,
            0.01723825, 0.02113206, 0.0564381 , 0.08126259, 0.05242541,
            0.03021909, 0.02431388, 0.02123043, 0.0206598 , 0.02689429,
            0.11548429, 0.05985154, 0.04029989, 0.03258969, 0.03021909,
            0.02465443, 0.03400206, 0.10594271, 0.05432308, 0.04029989,
            0.03294924, 0.02966876, 0.0264075 , 0.03858955, 0.450883  ,
            0.13890982, 0.05071048, 0.03830105, 0.03065231, 0.02684441,
            0.02818066, 0.04133261, 0.76257244, 0.10594271, 0.05472744,
            0.03400206, 0.02664759, 0.02636025, 0.03014864, 0.05735453,
            0.450883  , 0.07877603, 0.05556342, 0.03632324, 0.0270456 ,
            0.02669639, 0.03462002, 0.06331539, 0.1844543 , 0.10072007,
            0.05206877, 0.03997224, 0.03007868, 0.03141716, 0.04063561,
            0.09837397, 0.21943445, 0.10594271, 0.06331539, 0.04543852,
            0.0384445 , 0.03888458, 0.06597991, 0.34125893, 0.21943445,
            0.16169849, 0.07341788, 0.06744147, 0.08126259, 0.13890982,
            0.34125893, 0.450883  , 0.24560444, 0.0724687 , 0.03370508,
            0.02258748, 0.76257244, 0.28281631, 0.34125893, 0.450883  ,
            0.450883  , 0.1844543 , 0.08126259, 0.04452122, 0.02664759,
            0.24560444, 0.76257244, 0.24560444, 0.450883  , 0.1844543 ,
            0.08546177, 0.06094361, 0.04692537, 0.11548429, 0.12801398,
            0.09837397, 0.1844543 , 0.76257244, 0.76257244, 0.76257244,
            0.16169849, 0.09036205, 0.1844543 , 0.76257244, 0.76257244,
            0.34125893, 0.13890982, 0.76257244
           ]

right = [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
         0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
         0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
         0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
         0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
         0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
         0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
         0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
         0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
         0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
         0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
         0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
         0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
         0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
         0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
         0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
         0.3, 0.3, 0.3, 0.5, 0.5, 0.5, 0.5, 0.3, 0.3, 0.3, 0.3, 0.3, 0.5,
         0.5, 0.5, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.5, 0.5,
         0.9, 0.9, 0.9, 0.9, 0.3, 0.3, 0.9, 0.9, 0.9
        ]

left = [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
        0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
        0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
        0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
        0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
        0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
        0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
        0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
        0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
        0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
        0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
        0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
        0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
        0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
        0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
        0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
        0.3, 0.3, 0.3, 0.5, 0.5, 0.5, 0.5, 0.3, 0.3, 0.3, 0.3, 0.3, 0.5,
        0.5, 0.5, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.5, 0.5,
        0.9, 0.9, 0.9, 0.9, 0.3, 0.3, 0.9, 0.9, 0.9
       ]

err_up2 = None

err_down2 = None

upper_lim = [False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False
            ]

lower_lim = [False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False, False
            ]
