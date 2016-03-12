import json
stations = json.loads('''[
  {
    "id": 2,
    "IsEtoStation": "True",
    "latitude": 36.336222,
    "longitude": -120.11291
  },
  {
    "id": 5,
    "IsEtoStation": "True",
    "latitude": 35.532556,
    "longitude": -119.28179
  },
  {
    "id": 6,
    "IsEtoStation": "True",
    "latitude": 38.535694,
    "longitude": -121.77636
  },
  {
    "id": 7,
    "IsEtoStation": "True",
    "latitude": 36.851222,
    "longitude": -120.59092
  },
  {
    "id": 12,
    "IsEtoStation": "True",
    "latitude": 39.608639,
    "longitude": -121.82443
  },
  {
    "id": 13,
    "IsEtoStation": "True",
    "latitude": 38.753136,
    "longitude": -120.7336
  },
  {
    "id": 15,
    "IsEtoStation": "True",
    "latitude": 36.157972,
    "longitude": -119.85143
  },
  {
    "id": 21,
    "IsEtoStation": "True",
    "latitude": 35.86775,
    "longitude": -119.8949
  },
  {
    "id": 32,
    "IsEtoStation": "True",
    "latitude": 39.226861,
    "longitude": -122.0248
  },
  {
    "id": 35,
    "IsEtoStation": "True",
    "latitude": 37.358514,
    "longitude": -118.40553
  },
  {
    "id": 39,
    "IsEtoStation": "True",
    "latitude": 36.597444,
    "longitude": -119.50404
  },
  {
    "id": 41,
    "IsEtoStation": "True",
    "latitude": 33.042986,
    "longitude": -115.41585
  },
  {
    "id": 43,
    "IsEtoStation": "True",
    "latitude": 41.063767,
    "longitude": -121.45602
  },
  {
    "id": 44,
    "IsEtoStation": "True",
    "latitude": 33.964942,
    "longitude": -117.33698
  },
  {
    "id": 47,
    "IsEtoStation": "True",
    "latitude": 37.928258,
    "longitude": -121.6599
  },
  {
    "id": 52,
    "IsEtoStation": "True",
    "latitude": 35.305442,
    "longitude": -120.66178
  },
  {
    "id": 54,
    "IsEtoStation": "True",
    "latitude": 35.649861,
    "longitude": -119.9593
  },
  {
    "id": 56,
    "IsEtoStation": "True",
    "latitude": 37.096694,
    "longitude": -120.7539
  },
  {
    "id": 57,
    "IsEtoStation": "True",
    "latitude": 40.289953,
    "longitude": -120.4349
  },
  {
    "id": 62,
    "IsEtoStation": "True",
    "latitude": 33.48665,
    "longitude": -117.22827
  },
  {
    "id": 64,
    "IsEtoStation": "True",
    "latitude": 34.583144,
    "longitude": -120.07924
  },
  {
    "id": 68,
    "IsEtoStation": "True",
    "latitude": 32.759575,
    "longitude": -115.73207
  },
  {
    "id": 70,
    "IsEtoStation": "True",
    "latitude": 37.834822,
    "longitude": -121.22319
  },
  {
    "id": 71,
    "IsEtoStation": "True",
    "latitude": 37.645222,
    "longitude": -121.18776
  },
  {
    "id": 75,
    "IsEtoStation": "True",
    "latitude": 33.68845,
    "longitude": -117.72118
  },
  {
    "id": 77,
    "IsEtoStation": "True",
    "latitude": 38.428475,
    "longitude": -122.41021
  },
  {
    "id": 78,
    "IsEtoStation": "True",
    "latitude": 34.056589,
    "longitude": -117.81307
  },
  {
    "id": 80,
    "IsEtoStation": "True",
    "latitude": 36.820833,
    "longitude": -119.74231
  },
  {
    "id": 83,
    "IsEtoStation": "True",
    "latitude": 38.40355,
    "longitude": -122.79993
  },
  {
    "id": 84,
    "IsEtoStation": "True",
    "latitude": 39.252561,
    "longitude": -121.31567
  },
  {
    "id": 86,
    "IsEtoStation": "True",
    "latitude": 36.3605,
    "longitude": -119.05935
  },
  {
    "id": 87,
    "IsEtoStation": "True",
    "latitude": 32.806183,
    "longitude": -115.44626
  },
  {
    "id": 88,
    "IsEtoStation": "True",
    "latitude": 34.942525,
    "longitude": -119.6738
  },
  {
    "id": 90,
    "IsEtoStation": "True",
    "latitude": 41.438214,
    "longitude": -120.48031
  },
  {
    "id": 91,
    "IsEtoStation": "True",
    "latitude": 41.958869,
    "longitude": -121.47237
  },
  {
    "id": 94,
    "IsEtoStation": "True",
    "latitude": 34.471333,
    "longitude": -119.86929
  },
  {
    "id": 99,
    "IsEtoStation": "True",
    "latitude": 34.044311,
    "longitude": -118.47689
  },
  {
    "id": 104,
    "IsEtoStation": "True",
    "latitude": 36.997444,
    "longitude": -121.99676
  },
  {
    "id": 105,
    "IsEtoStation": "True",
    "latitude": 36.634028,
    "longitude": -120.38181
  },
  {
    "id": 106,
    "IsEtoStation": "True",
    "latitude": 38.982581,
    "longitude": -123.08928
  },
  {
    "id": 107,
    "IsEtoStation": "True",
    "latitude": 34.437353,
    "longitude": -119.73742
  },
  {
    "id": 109,
    "IsEtoStation": "True",
    "latitude": 38.219503,
    "longitude": -122.35496
  },
  {
    "id": 113,
    "IsEtoStation": "True",
    "latitude": 36.121083,
    "longitude": -121.08457
  },
  {
    "id": 114,
    "IsEtoStation": "True",
    "latitude": 36.347306,
    "longitude": -121.29135
  },
  {
    "id": 116,
    "IsEtoStation": "True",
    "latitude": 36.716806,
    "longitude": -121.69189
  },
  {
    "id": 117,
    "IsEtoStation": "True",
    "latitude": 34.475914,
    "longitude": -117.26351
  },
  {
    "id": 121,
    "IsEtoStation": "True",
    "latitude": 38.415564,
    "longitude": -121.78691
  },
  {
    "id": 124,
    "IsEtoStation": "True",
    "latitude": 36.890056,
    "longitude": -120.73141
  },
  {
    "id": 125,
    "IsEtoStation": "True",
    "latitude": 35.205583,
    "longitude": -118.77841
  },
  {
    "id": 126,
    "IsEtoStation": "True",
    "latitude": 36.854833,
    "longitude": -121.36275
  },
  {
    "id": 129,
    "IsEtoStation": "True",
    "latitude": 36.902778,
    "longitude": -121.74193
  },
  {
    "id": 131,
    "IsEtoStation": "True",
    "latitude": 38.649964,
    "longitude": -121.21887
  },
  {
    "id": 135,
    "IsEtoStation": "True",
    "latitude": 33.662869,
    "longitude": -114.55811
  },
  {
    "id": 136,
    "IsEtoStation": "True",
    "latitude": 33.523694,
    "longitude": -116.15575
  },
  {
    "id": 140,
    "IsEtoStation": "True",
    "latitude": 38.116125,
    "longitude": -121.65921
  },
  {
    "id": 142,
    "IsEtoStation": "True",
    "latitude": 36.721083,
    "longitude": -119.38903
  },
  {
    "id": 143,
    "IsEtoStation": "True",
    "latitude": 36.822861,
    "longitude": -121.46787
  },
  {
    "id": 144,
    "IsEtoStation": "True",
    "latitude": 38.266428,
    "longitude": -122.61646
  },
  {
    "id": 146,
    "IsEtoStation": "True",
    "latitude": 35.505833,
    "longitude": -119.69114
  },
  {
    "id": 147,
    "IsEtoStation": "True",
    "latitude": 32.628208,
    "longitude": -116.93928
  },
  {
    "id": 148,
    "IsEtoStation": "True",
    "latitude": 37.314139,
    "longitude": -120.3867
  },
  {
    "id": 150,
    "IsEtoStation": "True",
    "latitude": 32.885847,
    "longitude": -117.14314
  },
  {
    "id": 151,
    "IsEtoStation": "True",
    "latitude": 33.532222,
    "longitude": -114.63389
  },
  {
    "id": 152,
    "IsEtoStation": "True",
    "latitude": 34.219386,
    "longitude": -118.99244
  },
  {
    "id": 153,
    "IsEtoStation": "True",
    "latitude": 33.08105,
    "longitude": -116.9757
  },
  {
    "id": 156,
    "IsEtoStation": "True",
    "latitude": 34.233639,
    "longitude": -119.19692
  },
  {
    "id": 157,
    "IsEtoStation": "True",
    "latitude": 37.995478,
    "longitude": -122.467656
  },
  {
    "id": 158,
    "IsEtoStation": "True",
    "latitude": 38.419439,
    "longitude": -122.65872
  },
  {
    "id": 159,
    "IsEtoStation": "True",
    "latitude": 34.146372,
    "longitude": -117.9858
  },
  {
    "id": 160,
    "IsEtoStation": "True",
    "latitude": 35.335261,
    "longitude": -120.73588
  },
  {
    "id": 161,
    "IsEtoStation": "True",
    "latitude": 37.438944,
    "longitude": -121.13851
  },
  {
    "id": 163,
    "IsEtoStation": "True",
    "latitude": 35.472556,
    "longitude": -120.64814
  },
  {
    "id": 165,
    "IsEtoStation": "True",
    "latitude": 34.841878,
    "longitude": -120.21274
  },
  {
    "id": 167,
    "IsEtoStation": "True",
    "latitude": 37.725881,
    "longitude": -121.47552
  },
  {
    "id": 169,
    "IsEtoStation": "True",
    "latitude": 36.082056,
    "longitude": -119.09342
  },
  {
    "id": 170,
    "IsEtoStation": "True",
    "latitude": 38.015372,
    "longitude": -122.02028
  },
  {
    "id": 171,
    "IsEtoStation": "True",
    "latitude": 37.598758,
    "longitude": -122.05323
  },
  {
    "id": 173,
    "IsEtoStation": "True",
    "latitude": 32.901867,
    "longitude": -117.25046
  },
  {
    "id": 174,
    "IsEtoStation": "True",
    "latitude": 33.798697,
    "longitude": -118.09479
  },
  {
    "id": 175,
    "IsEtoStation": "True",
    "latitude": 33.383697,
    "longitude": -114.71921
  },
  {
    "id": 178,
    "IsEtoStation": "True",
    "latitude": 37.837614,
    "longitude": -122.14074
  },
  {
    "id": 179,
    "IsEtoStation": "True",
    "latitude": 33.663325,
    "longitude": -117.09338
  },
  {
    "id": 181,
    "IsEtoStation": "True",
    "latitude": 33.078611,
    "longitude": -115.66056
  },
  {
    "id": 182,
    "IsEtoStation": "True",
    "latitude": 35.833,
    "longitude": -119.25596
  },
  {
    "id": 184,
    "IsEtoStation": "True",
    "latitude": 32.729578,
    "longitude": -117.13934
  },
  {
    "id": 187,
    "IsEtoStation": "True",
    "latitude": 38.090933,
    "longitude": -122.5267
  },
  {
    "id": 188,
    "IsEtoStation": "True",
    "latitude": 37.02,
    "longitude": -120.15
  },
  {
    "id": 191,
    "IsEtoStation": "True",
    "latitude": 37.663969,
    "longitude": -121.88503
  },
  {
    "id": 192,
    "IsEtoStation": "True",
    "latitude": 34.255942,
    "longitude": -117.21814
  },
  {
    "id": 193,
    "IsEtoStation": "True",
    "latitude": 36.633222,
    "longitude": -121.93486
  },
  {
    "id": 194,
    "IsEtoStation": "True",
    "latitude": 37.727194,
    "longitude": -120.85086
  },
  {
    "id": 195,
    "IsEtoStation": "True",
    "latitude": 38.887603,
    "longitude": -121.10291
  },
  {
    "id": 196,
    "IsEtoStation": "True",
    "latitude": 38.691786,
    "longitude": -122.01381
  },
  {
    "id": 197,
    "IsEtoStation": "True",
    "latitude": 34.614981,
    "longitude": -118.03249
  },
  {
    "id": 198,
    "IsEtoStation": "True",
    "latitude": 34.324639,
    "longitude": -119.10488
  },
  {
    "id": 199,
    "IsEtoStation": "True",
    "latitude": 34.237419,
    "longitude": -116.86571
  },
  {
    "id": 200,
    "IsEtoStation": "True",
    "latitude": 33.748586,
    "longitude": -116.2529
  },
  {
    "id": 202,
    "IsEtoStation": "True",
    "latitude": 35.028281,
    "longitude": -120.56003
  },
  {
    "id": 204,
    "IsEtoStation": "True",
    "latitude": 34.426361,
    "longitude": -118.51758
  },
  {
    "id": 205,
    "IsEtoStation": "True",
    "latitude": 36.175833,
    "longitude": -120.36027
  },
  {
    "id": 206,
    "IsEtoStation": "True",
    "latitude": 37.545869,
    "longitude": -120.75453
  },
  {
    "id": 207,
    "IsEtoStation": "True",
    "latitude": 33.268447,
    "longitude": -116.36505
  },
  {
    "id": 208,
    "IsEtoStation": "True",
    "latitude": 33.678186,
    "longitude": -116.27299
  },
  {
    "id": 209,
    "IsEtoStation": "True",
    "latitude": 36.913083,
    "longitude": -121.82365
  },
  {
    "id": 210,
    "IsEtoStation": "True",
    "latitude": 36.540889,
    "longitude": -121.88196
  },
  {
    "id": 211,
    "IsEtoStation": "True",
    "latitude": 37.015026,
    "longitude": -121.53704
  },
  {
    "id": 212,
    "IsEtoStation": "True",
    "latitude": 38.278056,
    "longitude": -121.74111
  },
  {
    "id": 213,
    "IsEtoStation": "True",
    "latitude": 37.931539,
    "longitude": -122.302714
  },
  {
    "id": 214,
    "IsEtoStation": "True",
    "latitude": 36.625619,
    "longitude": -121.537889
  },
  {
    "id": 215,
    "IsEtoStation": "True",
    "latitude": 34.291331,
    "longitude": -118.57004
  },
  {
    "id": 216,
    "IsEtoStation": "True",
    "latitude": 34.256111,
    "longitude": -118.38278
  },
  {
    "id": 217,
    "IsEtoStation": "True",
    "latitude": 34.269031,
    "longitude": -118.849319
  },
  {
    "id": 218,
    "IsEtoStation": "True",
    "latitude": 33.595694,
    "longitude": -116.15811
  },
  {
    "id": 219,
    "IsEtoStation": "True",
    "latitude": 34.214197,
    "longitude": -118.64477
  },
  {
    "id": 220,
    "IsEtoStation": "True",
    "latitude": 34.592222,
    "longitude": -118.1275
  },
  {
    "id": 221,
    "IsEtoStation": "True",
    "latitude": 34.513611,
    "longitude": -115.51056
  },
  {
    "id": 222,
    "IsEtoStation": "True",
    "latitude": 40.028778,
    "longitude": -122.15575
  },
  {
    "id": 225,
    "IsEtoStation": "True",
    "latitude": 41.577778,
    "longitude": -122.838125
  },
  {
    "id": 226,
    "IsEtoStation": "True",
    "latitude": 38.672722,
    "longitude": -121.81172
  },
  {
    "id": 227,
    "IsEtoStation": "True",
    "latitude": 38.508333,
    "longitude": -120.79972
  },
  {
    "id": 228,
    "IsEtoStation": "True",
    "latitude": 38.636111,
    "longitude": -120.79305
  },
  {
    "id": 229,
    "IsEtoStation": "True",
    "latitude": 36.570111,
    "longitude": -121.7865
  },
  {
    "id": 232,
    "IsEtoStation": "True",
    "latitude": 34.913472,
    "longitude": -120.46478
  },
  {
    "id": 234,
    "IsEtoStation": "True",
    "latitude": 34.883472,
    "longitude": -116.810247
  },
  {
    "id": 235,
    "IsEtoStation": "True",
    "latitude": 38.797944,
    "longitude": -121.61136
  },
  {
    "id": 236,
    "IsEtoStation": "True",
    "latitude": 41.802476,
    "longitude": -121.996159
  },
  {
    "id": 237,
    "IsEtoStation": "True",
    "latitude": 33.55,
    "longitude": -117.04
  },
  {
    "id": 238,
    "IsEtoStation": "True",
    "latitude": 33.9,
    "longitude": -117.17
  },
  {
    "id": 239,
    "IsEtoStation": "True",
    "latitude": 33.664747,
    "longitude": -116.955121
  },
  {
    "id": 240,
    "IsEtoStation": "True",
    "latitude": 33.76,
    "longitude": -117.2
  },
  {
    "id": 241,
    "IsEtoStation": "True",
    "latitude": 33.4625,
    "longitude": -117.586111
  },
  {
    "id": 242,
    "IsEtoStation": "True",
    "latitude": 38.192397,
    "longitude": -121.510261
  },
  {
    "id": 244,
    "IsEtoStation": "True",
    "latitude": 39.386632,
    "longitude": -121.835278
  },
  {
    "id": 245,
    "IsEtoStation": "True",
    "latitude": 33.621667,
    "longitude": -117.585278
  },
  {
    "id": 19,
    "IsEtoStation": "False",
    "latitude": 36.768167,
    "longitude": -121.77364
  },
  {
    "id": 85,
    "IsEtoStation": "False",
    "latitude": 39.006747,
    "longitude": -123.08012
  },
  {
    "id": 92,
    "IsEtoStation": "False",
    "latitude": 37.231861,
    "longitude": -120.88082
  },
  {
    "id": 103,
    "IsEtoStation": "False",
    "latitude": 38.526336,
    "longitude": -122.8293
  },
  {
    "id": 111,
    "IsEtoStation": "False",
    "latitude": 36.943964,
    "longitude": -121.76394
  },
  {
    "id": 139,
    "IsEtoStation": "False",
    "latitude": 38.501258,
    "longitude": -121.97853
  },
  {
    "id": 155,
    "IsEtoStation": "False",
    "latitude": 38.599158,
    "longitude": -121.54041
  },
  {
    "id": 183,
    "IsEtoStation": "False",
    "latitude": 36.488611,
    "longitude": -117.91944
  },
  {
    "id": 189,
    "IsEtoStation": "False",
    "latitude": 36.358628,
    "longitude": -117.94387
  },
  {
    "id": 190,
    "IsEtoStation": "False",
    "latitude": 36.382028,
    "longitude": -120.22985
  },
  {
    "id": 203,
    "IsEtoStation": "False",
    "latitude": 35.862583,
    "longitude": -119.50357
  },
  {
    "id": 224,
    "IsEtoStation": "False",
    "latitude": 40.63,
    "longitude": -122.31
  },
  {
    "id": 230,
    "IsEtoStation": "False",
    "latitude": 34.405556,
    "longitude": -119.715
  },
  {
    "id": 231,
    "IsEtoStation": "False",
    "latitude": 34.672222,
    "longitude": -120.51306
  },
  {
    "id": 233,
    "IsEtoStation": "False",
    "latitude": 34.138147,
    "longitude": -116.21319
  }
]''')
