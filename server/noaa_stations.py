import json
stations = json.loads('''[
  {
    "latitude": 38.3775,
    "id": "GHCND:USC00049582",
    "longitude": -120.5452
  },
  {
    "latitude": 37.3711,
    "id": "GHCND:USW00023157",
    "longitude": -118.358
  },
  {
    "latitude": 34.98833,
    "id": "GHCND:USW00053144",
    "longitude": -117.86472
  },
  {
    "latitude": 35.3056,
    "id": "GHCND:USC00047851",
    "longitude": -120.6619
  },
  {
    "latitude": 37.72139,
    "id": "GHCND:USW00023230",
    "longitude": -122.22083
  },
  {
    "latitude": 39.165,
    "id": "GHCND:USC00043491",
    "longitude": -120.8566
  },
  {
    "latitude": 39.3886,
    "id": "GHCND:USC00040931",
    "longitude": -120.0936
  },
  {
    "latitude": 40.7367,
    "id": "GHCND:USC00049490",
    "longitude": -122.9404
  },
  {
    "latitude": 39.5091,
    "id": "GHCND:USC00043161",
    "longitude": -123.7566
  },
  {
    "latitude": 37.4767,
    "id": "GHCND:USC00047339",
    "longitude": -122.2386
  },
  {
    "latitude": 39.1266,
    "id": "GHCND:USC00049124",
    "longitude": -123.2719
  },
  {
    "latitude": 34.5883,
    "id": "GHCND:USC00046624",
    "longitude": -118.0938
  },
  {
    "latitude": 35.0233,
    "id": "GHCND:USC00048839",
    "longitude": -118.7497
  },
  {
    "latitude": 33.7086,
    "id": "GHCND:USC00044259",
    "longitude": -116.2152
  },
  {
    "latitude": 40.4167,
    "id": "GHCND:USC00048702",
    "longitude": -120.6631
  },
  {
    "latitude": 34.01583,
    "id": "GHCND:USW00093197",
    "longitude": -118.45139
  },
  {
    "latitude": 35.1011,
    "id": "GHCND:USC00048829",
    "longitude": -118.4222
  },
  {
    "latitude": 36.9969,
    "id": "GHCND:USC00043261",
    "longitude": -119.7072
  },
  {
    "latitude": 40.9466,
    "id": "GHCND:USC00049694",
    "longitude": -123.6363
  },
  {
    "latitude": 37.0563,
    "id": "GHCND:USC00045118",
    "longitude": -120.8666
  },
  {
    "latitude": 37.9672,
    "id": "GHCND:USC00048353",
    "longitude": -120.3872
  },
  {
    "latitude": 34.1483,
    "id": "GHCND:USC00046719",
    "longitude": -118.1447
  },
  {
    "latitude": 37.6241,
    "id": "GHCND:USW00023258",
    "longitude": -120.9505
  },
  {
    "latitude": 39.2774,
    "id": "GHCND:USW00023225",
    "longitude": -120.7102
  },
  {
    "latitude": 38.9238,
    "id": "GHCND:USC00041806",
    "longitude": -122.5672
  },
  {
    "latitude": 41.7036,
    "id": "GHCND:USC00049866",
    "longitude": -122.6408
  },
  {
    "latitude": 32.8672,
    "id": "GHCND:USC00045968",
    "longitude": -116.4194
  },
  {
    "latitude": 37.2329,
    "id": "GHCND:USC00046252",
    "longitude": -119.5097
  },
  {
    "latitude": 33.7442,
    "id": "GHCND:USC00047888",
    "longitude": -117.8667
  },
  {
    "latitude": 41.6,
    "id": "GHCND:USC00043182",
    "longitude": -122.8478
  },
  {
    "latitude": 39.9366,
    "id": "GHCND:USC00047195",
    "longitude": -120.9475
  },
  {
    "latitude": 36.3642,
    "id": "GHCND:USC00043083",
    "longitude": -120.1561
  },
  {
    "latitude": 37.8891,
    "id": "GHCND:USW00023237",
    "longitude": -121.2258
  },
  {
    "latitude": 39.5833,
    "id": "GHCND:USC00048218",
    "longitude": -120.3705
  },
  {
    "latitude": 33.8275,
    "id": "GHCND:USC00046635",
    "longitude": -116.5097
  },
  {
    "latitude": 38.5349,
    "id": "GHCND:USC00042294",
    "longitude": -121.7761
  },
  {
    "latitude": 33.8116,
    "id": "GHCND:USW00023129",
    "longitude": -118.1463
  },
  {
    "latitude": 38.573,
    "id": "GHCND:USC00040212",
    "longitude": -122.4405
  },
  {
    "latitude": 34.2903,
    "id": "GHCND:USC00046699",
    "longitude": -114.1708
  },
  {
    "latitude": 36.3278,
    "id": "GHCND:USC00049367",
    "longitude": -119.2994
  },
  {
    "latitude": 38.933,
    "id": "GHCND:USC00043384",
    "longitude": -120.8008
  },
  {
    "latitude": 36.78,
    "id": "GHCND:USW00093193",
    "longitude": -119.7194
  },
  {
    "latitude": 33.121,
    "id": "GHCND:USC00042863",
    "longitude": -117.09
  },
  {
    "latitude": 40.3033,
    "id": "GHCND:USC00041700",
    "longitude": -121.2422
  },
  {
    "latitude": 34.5894,
    "id": "GHCND:USC00048014",
    "longitude": -118.4547
  },
  {
    "latitude": 35.3741,
    "id": "GHCND:USC00047933",
    "longitude": -120.6375
  },
  {
    "latitude": 36.9308,
    "id": "GHCND:USC00049473",
    "longitude": -121.7691
  },
  {
    "latitude": 34.0236,
    "id": "GHCND:USW00093134",
    "longitude": -118.2911
  },
  {
    "latitude": 37.75,
    "id": "GHCND:USC00049855",
    "longitude": -119.5897
  },
  {
    "latitude": 39.01,
    "id": "GHCND:USC00043134",
    "longitude": -120.8455
  },
  {
    "latitude": 36.2472,
    "id": "GHCND:USC00040790",
    "longitude": -121.7802
  },
  {
    "latitude": 38.3858,
    "id": "GHCND:USC00046370",
    "longitude": -122.9661
  },
  {
    "latitude": 36.3158,
    "id": "GHCND:USC00043747",
    "longitude": -119.637
  },
  {
    "latitude": 32.86667,
    "id": "GHCND:USW00093107",
    "longitude": -117.13333
  },
  {
    "latitude": 34.4061,
    "id": "GHCND:USC00046940",
    "longitude": -118.7569
  },
  {
    "latitude": 33.2559,
    "id": "GHCND:USC00040983",
    "longitude": -116.4036
  },
  {
    "latitude": 34.9455,
    "id": "GHCND:USC00046154",
    "longitude": -119.6827
  },
  {
    "latitude": 33.6131,
    "id": "GHCND:USC00040924",
    "longitude": -114.5972
  },
  {
    "latitude": 32.8005,
    "id": "GHCND:USC00042706",
    "longitude": -116.928
  },
  {
    "latitude": 39.8053,
    "id": "GHCND:USC00047085",
    "longitude": -120.4719
  },
  {
    "latitude": 34.005,
    "id": "GHCND:USC00042214",
    "longitude": -118.4139
  },
  {
    "latitude": 39.1678,
    "id": "GHCND:USC00048758",
    "longitude": -120.1428
  },
  {
    "latitude": 38.2777,
    "id": "GHCND:USC00046074",
    "longitude": -122.2647
  },
  {
    "latitude": 35.2111,
    "id": "GHCND:USC00040332",
    "longitude": -118.8336
  },
  {
    "latitude": 35.6277,
    "id": "GHCND:USC00046730",
    "longitude": -120.6855
  },
  {
    "latitude": 36.33333,
    "id": "GHCND:USW00023110",
    "longitude": -119.95
  },
  {
    "latitude": 37.40583,
    "id": "GHCND:USW00023244",
    "longitude": -122.04806
  },
  {
    "latitude": 41.5305,
    "id": "GHCND:USC00041614",
    "longitude": -120.1804
  },
  {
    "latitude": 37.5122,
    "id": "GHCND:USC00048380",
    "longitude": -119.6331
  },
  {
    "latitude": 38.9072,
    "id": "GHCND:USC00040383",
    "longitude": -121.0838
  },
  {
    "latitude": 32.8358,
    "id": "GHCND:USC00040136",
    "longitude": -116.7774
  },
  {
    "latitude": 35.4186,
    "id": "GHCND:USC00040444",
    "longitude": -119.0508
  },
  {
    "latitude": 41.2514,
    "id": "GHCND:USC00045449",
    "longitude": -122.1383
  },
  {
    "latitude": 34.8328,
    "id": "GHCND:USC00044863",
    "longitude": -118.865
  },
  {
    "latitude": 32.7,
    "id": "GHCND:USW00093112",
    "longitude": -117.2
  },
  {
    "latitude": 37.4436,
    "id": "GHCND:USC00046646",
    "longitude": -122.1402
  },
  {
    "latitude": 37.2858,
    "id": "GHCND:USC00045532",
    "longitude": -120.5117
  },
  {
    "latitude": 36.4819,
    "id": "GHCND:USC00046926",
    "longitude": -121.1822
  },
  {
    "latitude": 35.5892,
    "id": "GHCND:USC00049452",
    "longitude": -119.352
  },
  {
    "latitude": 34.1553,
    "id": "GHCND:USC00047776",
    "longitude": -117.9078
  },
  {
    "latitude": 34.1061,
    "id": "GHCND:USC00047785",
    "longitude": -118.1
  },
  {
    "latitude": 37.79833,
    "id": "GHCND:USC00046336",
    "longitude": -122.26417
  },
  {
    "latitude": 41.8452,
    "id": "GHCND:USC00043357",
    "longitude": -123.9647
  },
  {
    "latitude": 38.5069,
    "id": "GHCND:USW00023232",
    "longitude": -121.495
  },
  {
    "latitude": 37.4725,
    "id": "GHCND:USC00043714",
    "longitude": -122.44333
  },
  {
    "latitude": 37.3133,
    "id": "GHCND:USC00048273",
    "longitude": -122.185
  },
  {
    "latitude": 36.7672,
    "id": "GHCND:USC00043256",
    "longitude": -119.7092
  },
  {
    "latitude": 35.7636,
    "id": "GHCND:USC00049035",
    "longitude": -117.3908
  },
  {
    "latitude": 37.6478,
    "id": "GHCND:USC00045280",
    "longitude": -118.9617
  },
  {
    "latitude": 40.1519,
    "id": "GHCND:USW00024216",
    "longitude": -122.2536
  },
  {
    "latitude": 40.54111,
    "id": "GHCND:USC00045311",
    "longitude": -121.57667
  },
  {
    "latitude": 34.4258,
    "id": "GHCND:USW00023190",
    "longitude": -119.8425
  },
  {
    "latitude": 37.9566,
    "id": "GHCND:USC00044500",
    "longitude": -122.5447
  },
  {
    "latitude": 34.4167,
    "id": "GHCND:USC00047902",
    "longitude": -119.6844
  },
  {
    "latitude": 41.3206,
    "id": "GHCND:USC00045983",
    "longitude": -122.3081
  },
  {
    "latitude": 36.9092,
    "id": "GHCND:USC00040449",
    "longitude": -119.0883
  },
  {
    "latitude": 38.8983,
    "id": "GHCND:USW00093230",
    "longitude": -119.9947
  },
  {
    "latitude": 39.8716,
    "id": "GHCND:USC00042402",
    "longitude": -121.6108
  },
  {
    "latitude": 33.92278,
    "id": "GHCND:USW00003167",
    "longitude": -118.33417
  },
  {
    "latitude": 33.8016,
    "id": "GHCND:USW00003122",
    "longitude": -118.3419
  },
  {
    "latitude": 37.5422,
    "id": "GHCND:USC00043244",
    "longitude": -122.0158
  },
  {
    "latitude": 40.6116,
    "id": "GHCND:USC00049621",
    "longitude": -122.528
  },
  {
    "latitude": 32.6261,
    "id": "GHCND:USW00003164",
    "longitude": -116.4681
  },
  {
    "latitude": 34.3591,
    "id": "GHCND:USC00044394",
    "longitude": -116.5378
  },
  {
    "latitude": 34.8927,
    "id": "GHCND:USC00040521",
    "longitude": -117.0219
  },
  {
    "latitude": 36.1356,
    "id": "GHCND:USC00041864",
    "longitude": -120.3606
  },
  {
    "latitude": 41.96,
    "id": "GHCND:USC00049053",
    "longitude": -121.4744
  },
  {
    "latitude": 39.3619,
    "id": "GHCND:USC00047109",
    "longitude": -123.1286
  },
  {
    "latitude": 37.9567,
    "id": "GHCND:USC00044881",
    "longitude": -119.1194
  },
  {
    "latitude": 35.3692,
    "id": "GHCND:USC00047253",
    "longitude": -117.6525
  },
  {
    "latitude": 37.3436,
    "id": "GHCND:USC00045933",
    "longitude": -121.6425
  },
  {
    "latitude": 32.6263,
    "id": "GHCND:USC00041424",
    "longitude": -116.4699
  },
  {
    "latitude": 34.2308,
    "id": "GHCND:USC00046006",
    "longitude": -118.0711
  },
  {
    "latitude": 40.4,
    "id": "GHCND:USC00041907",
    "longitude": -122.1433
  },
  {
    "latitude": 33.7572,
    "id": "GHCND:USC00044211",
    "longitude": -116.7066
  },
  {
    "latitude": 35.7269,
    "id": "GHCND:USC00043463",
    "longitude": -118.7006
  },
  {
    "latitude": 36.3817,
    "id": "GHCND:USC00044890",
    "longitude": -119.0264
  },
  {
    "latitude": 34.4477,
    "id": "GHCND:USC00046399",
    "longitude": -119.2275
  },
  {
    "latitude": 41.3088,
    "id": "GHCND:USC00046508",
    "longitude": -123.5316
  },
  {
    "latitude": 36.6594,
    "id": "GHCND:USC00047668",
    "longitude": -121.6663
  },
  {
    "latitude": 39.7458,
    "id": "GHCND:USC00046506",
    "longitude": -122.1997
  },
  {
    "latitude": 36.7394,
    "id": "GHCND:USC00043551",
    "longitude": -118.9631
  },
  {
    "latitude": 39.523,
    "id": "GHCND:USC00049699",
    "longitude": -122.3058
  },
  {
    "latitude": 41.2683,
    "id": "GHCND:USC00044374",
    "longitude": -120.2947
  },
  {
    "latitude": 37.2319,
    "id": "GHCND:USC00045123",
    "longitude": -121.9592
  },
  {
    "latitude": 34.0528,
    "id": "GHCND:USC00047306",
    "longitude": -117.1894
  },
  {
    "latitude": 34.7436,
    "id": "GHCND:USW00023187",
    "longitude": -118.7242
  },
  {
    "latitude": 34.243,
    "id": "GHCND:USC00040741",
    "longitude": -116.917
  },
  {
    "latitude": 34.0697,
    "id": "GHCND:USC00049152",
    "longitude": -118.4427
  },
  {
    "latitude": 36.2032,
    "id": "GHCND:USC00044957",
    "longitude": -119.0545
  },
  {
    "latitude": 35.6841,
    "id": "GHCND:USC00043882",
    "longitude": -121.1683
  },
  {
    "latitude": 36.4914,
    "id": "GHCND:USC00040343",
    "longitude": -118.8253
  },
  {
    "latitude": 33.2372,
    "id": "GHCND:USC00043914",
    "longitude": -116.7614
  },
  {
    "latitude": 36.6044,
    "id": "GHCND:USC00045026",
    "longitude": -118.7325
  },
  {
    "latitude": 34.5822,
    "id": "GHCND:USC00041253",
    "longitude": -119.9817
  },
  {
    "latitude": 37.7967,
    "id": "GHCND:USC00049001",
    "longitude": -121.5828
  },
  {
    "latitude": 33.95194,
    "id": "GHCND:USW00003171",
    "longitude": -117.43861
  },
  {
    "latitude": 39.7538,
    "id": "GHCND:USC00046685",
    "longitude": -121.6241
  },
  {
    "latitude": 36.31889,
    "id": "GHCND:USW00053119",
    "longitude": -119.62889
  },
  {
    "latitude": 35.4028,
    "id": "GHCND:USC00041244",
    "longitude": -119.47
  },
  {
    "latitude": 39.5861,
    "id": "GHCND:USC00048587",
    "longitude": -122.5341
  },
  {
    "latitude": 39.2466,
    "id": "GHCND:USC00046136",
    "longitude": -121.0008
  },
  {
    "latitude": 38.492,
    "id": "GHCND:USC00044712",
    "longitude": -122.0039
  },
  {
    "latitude": 34.1866,
    "id": "GHCND:USC00041194",
    "longitude": -118.348
  },
  {
    "latitude": 38.3775,
    "id": "GHCND:USW00093241",
    "longitude": -121.9575
  },
  {
    "latitude": 34.128,
    "id": "GHCND:USC00049099",
    "longitude": -116.0369
  },
  {
    "latitude": 40.7263,
    "id": "GHCND:USC00049026",
    "longitude": -122.7947
  },
  {
    "latitude": 37.8792,
    "id": "GHCND:USC00045915",
    "longitude": -121.9303
  },
  {
    "latitude": 33.8089,
    "id": "GHCND:USC00042598",
    "longitude": -115.4508
  },
  {
    "latitude": 33.87194,
    "id": "GHCND:USW00003166",
    "longitude": -117.97889
  },
  {
    "latitude": 40.9869,
    "id": "GHCND:USC00046946",
    "longitude": -121.9772
  },
  {
    "latitude": 33.0375,
    "id": "GHCND:USW00053120",
    "longitude": -116.91583
  },
  {
    "latitude": 39.563,
    "id": "GHCND:USC00048606",
    "longitude": -121.1077
  },
  {
    "latitude": 33.7044,
    "id": "GHCND:USC00043855",
    "longitude": -115.6289
  },
  {
    "latitude": 34.1472,
    "id": "GHCND:USC00044297",
    "longitude": -115.1219
  },
  {
    "latitude": 36.9905,
    "id": "GHCND:USC00047916",
    "longitude": -121.9911
  },
  {
    "latitude": 37.9833,
    "id": "GHCND:USC00041967",
    "longitude": -122.0692
  },
  {
    "latitude": 34.7411,
    "id": "GHCND:USW00003159",
    "longitude": -118.2116
  },
  {
    "latitude": 40.48306,
    "id": "GHCND:USC00048045",
    "longitude": -124.10361
  },
  {
    "latitude": 36.5927,
    "id": "GHCND:USC00045802",
    "longitude": -121.8555
  },
  {
    "latitude": 33.938,
    "id": "GHCND:USW00023174",
    "longitude": -118.3888
  },
  {
    "latitude": 33.8647,
    "id": "GHCND:USC00040192",
    "longitude": -117.8425
  },
  {
    "latitude": 32.7669,
    "id": "GHCND:USC00042713",
    "longitude": -115.5617
  },
  {
    "latitude": 36.0975,
    "id": "GHCND:USC00042012",
    "longitude": -119.5817
  },
  {
    "latitude": 38.4916,
    "id": "GHCND:USC00045360",
    "longitude": -122.1241
  },
  {
    "latitude": 38.0047,
    "id": "GHCND:USC00046174",
    "longitude": -120.4863
  },
  {
    "latitude": 33.6186,
    "id": "GHCND:USW00023158",
    "longitude": -114.7142
  },
  {
    "latitude": 40.7141,
    "id": "GHCND:USC00048135",
    "longitude": -122.4161
  },
  {
    "latitude": 39.49,
    "id": "GHCND:USW00093210",
    "longitude": -121.61833
  },
  {
    "latitude": 33.8222,
    "id": "GHCND:USW00093138",
    "longitude": -116.5043
  },
  {
    "latitude": 34.7675,
    "id": "GHCND:USW00023179",
    "longitude": -114.6188
  },
  {
    "latitude": 34.2066,
    "id": "GHCND:USC00046572",
    "longitude": -119.1375
  },
  {
    "latitude": 33.62667,
    "id": "GHCND:USW00003104",
    "longitude": -116.15944
  },
  {
    "latitude": 36.602,
    "id": "GHCND:USW00053139",
    "longitude": -117.1449
  },
  {
    "latitude": 40.97806,
    "id": "GHCND:USW00024283",
    "longitude": -124.10861
  },
  {
    "latitude": 38.3208,
    "id": "GHCND:USW00093245",
    "longitude": -123.0747
  },
  {
    "latitude": 41.49139,
    "id": "GHCND:USW00094299",
    "longitude": -120.56444
  },
  {
    "latitude": 36.98778,
    "id": "GHCND:USW00093242",
    "longitude": -120.11056
  },
  {
    "latitude": 33.6617,
    "id": "GHCND:USC00041738",
    "longitude": -115.7206
  },
  {
    "latitude": 40.6507,
    "id": "GHCND:USW00004222",
    "longitude": -122.6068
  },
  {
    "latitude": 32.57222,
    "id": "GHCND:USW00003178",
    "longitude": -116.97944
  },
  {
    "latitude": 36.93583,
    "id": "GHCND:USW00023277",
    "longitude": -121.78861
  },
  {
    "latitude": 37.2381,
    "id": "GHCND:USW00093243",
    "longitude": -120.8825
  },
  {
    "latitude": 33.97528,
    "id": "GHCND:USW00003179",
    "longitude": -117.63611
  },
  {
    "latitude": 41.9797,
    "id": "GHCND:USC00041990",
    "longitude": -122.3378
  },
  {
    "latitude": 32.81583,
    "id": "GHCND:USW00003131",
    "longitude": -117.13944
  },
  {
    "latitude": 41.3325,
    "id": "GHCND:USW00024215",
    "longitude": -122.33278
  },
  {
    "latitude": 39.2041,
    "id": "GHCND:USC00043573",
    "longitude": -121.068
  },
  {
    "latitude": 33.21944,
    "id": "GHCND:USW00053121",
    "longitude": -117.34944
  },
  {
    "latitude": 34.4141,
    "id": "GHCND:USW00053152",
    "longitude": -119.8796
  },
  {
    "latitude": 34.20083,
    "id": "GHCND:USW00093110",
    "longitude": -119.20694
  },
  {
    "latitude": 33.68,
    "id": "GHCND:USW00093184",
    "longitude": -117.86639
  },
  {
    "latitude": 38.69556,
    "id": "GHCND:USW00093225",
    "longitude": -121.58972
  },
  {
    "latitude": 37.7592,
    "id": "GHCND:USW00053150",
    "longitude": -119.8208
  },
  {
    "latitude": 34.1819,
    "id": "GHCND:USC00049785",
    "longitude": -118.5744
  },
  {
    "latitude": 37.28472,
    "id": "GHCND:USW00023257",
    "longitude": -120.51278
  },
  {
    "latitude": 39.1019,
    "id": "GHCND:USW00093205",
    "longitude": -121.5677
  },
  {
    "latitude": 35.4867,
    "id": "GHCND:USC00048122",
    "longitude": -119.1458
  },
  {
    "latitude": 33.4392,
    "id": "GHCND:USW00053151",
    "longitude": -117.1904
  },
  {
    "latitude": 33.12806,
    "id": "GHCND:USW00003177",
    "longitude": -117.27944
  },
  {
    "latitude": 36.4622,
    "id": "GHCND:USC00042319",
    "longitude": -116.8669
  },
  {
    "latitude": 34.05611,
    "id": "GHCND:USW00003102",
    "longitude": -117.60028
  },
  {
    "latitude": 38.5552,
    "id": "GHCND:USW00023271",
    "longitude": -121.4183
  },
  {
    "latitude": 35.23722,
    "id": "GHCND:USW00093206",
    "longitude": -120.64139
  },
  {
    "latitude": 37.6197,
    "id": "GHCND:USW00023234",
    "longitude": -122.3647
  },
  {
    "latitude": 34.20056,
    "id": "GHCND:USW00023152",
    "longitude": -118.3575
  },
  {
    "latitude": 34.8536,
    "id": "GHCND:USW00023161",
    "longitude": -116.7858
  },
  {
    "latitude": 32.7336,
    "id": "GHCND:USW00023188",
    "longitude": -117.1831
  },
  {
    "latitude": 38.5038,
    "id": "GHCND:USW00023213",
    "longitude": -122.8102
  },
  {
    "latitude": 37.6927,
    "id": "GHCND:USW00023285",
    "longitude": -121.8144
  },
  {
    "latitude": 37.3591,
    "id": "GHCND:USW00023293",
    "longitude": -121.924
  },
  {
    "latitude": 37.9917,
    "id": "GHCND:USW00023254",
    "longitude": -122.055
  },
  {
    "latitude": 37.6542,
    "id": "GHCND:USW00093228",
    "longitude": -122.115
  },
  {
    "latitude": 38.2102,
    "id": "GHCND:USW00093227",
    "longitude": -122.2847
  },
  {
    "latitude": 34.8994,
    "id": "GHCND:USW00023273",
    "longitude": -120.4486
  },
  {
    "latitude": 40.5175,
    "id": "GHCND:USW00024257",
    "longitude": -122.2986
  },
  {
    "latitude": 35.6697,
    "id": "GHCND:USW00093209",
    "longitude": -120.6283
  },
  {
    "latitude": 37.7705,
    "id": "GHCND:USW00023272",
    "longitude": -122.4269
  },
  {
    "latitude": 34.08639,
    "id": "GHCND:USC00045860",
    "longitude": -116.56222
  },
  {
    "latitude": 34.12056,
    "id": "GHCND:USC00049102",
    "longitude": -115.85
  },
  {
    "latitude": 35.4344,
    "id": "GHCND:USW00023155",
    "longitude": -119.0542
  },
  {
    "latitude": 40.8097,
    "id": "GHCND:USW00024213",
    "longitude": -124.1602
  }
]
''')
