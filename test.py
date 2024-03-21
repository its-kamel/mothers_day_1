import mysql.connector
from oauth2client.service_account import ServiceAccountCredentials
import time
import requests
from datetime import datetime,timedelta
from bs4 import BeautifulSoup
import gspread
import pytz
import os
# Define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

current_dir = os.path.dirname(os.path.abspath(__file__))

# Add your credentials JSON file obtained from Google Developer Console
creds = ServiceAccountCredentials.from_json_keyfile_name(os.path.join(current_dir,'autofetch-1611435677959-a975f9d40d2c.json'), scope)

# Authorize the client
client = gspread.authorize(creds)

# Open the Google Sheet by ID
sheet = client.open_by_key('1IB5hgHo5IrARwCMGM9d-fQN5trXE0OSiGa-g-bVq-Rw')

# Select the first worksheet
worksheet = sheet.get_worksheet(0)

CIL_LOGIN_URL_APP = 'https://appadmin.cilantro.cafe/authpanel/login/checklogin'
CIL_PROMO_URL_APP = 'https://appadmin.cilantro.cafe/authpanel/promocode/add'
CIL_EMAIL_APP = "admin@cilantro.com"
CIL_PASSWORD_APP = "admin@123"

HEADER_APP = {
  "User-Agent":
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4515.107 Safari/537.36"
}

CIL_LOGIN_URL_OPPE = 'https://admin.cilantrocafe.net/admin/login'
CIL_PROMO_URL_OPPE = 'https://admin.cilantrocafe.net/admin/promocodes'
CIL_PROMO_CREATE_URL_OPPE = 'https://admin.cilantrocafe.net/admin/promocodes/create'
CIL_EMAIL_OPPE = "admin@cilantrocafe.net"
CIL_PASSWORD_OPPE = "Fck8UVK3kJF3ju4w"

HEADER_OPPE = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4515.107 Safari/537.36"
}



def generate_promo(name):
    QUERY_1 =f"""
    SELECT promocode FROM tbl_promocode order by insertdate desc
    """
    QUERY_2 =f"""
    SELECT code FROM cilantro.promocodes order by created_at desc """
    mydb = mysql.connector.connect(
    host="cliantro.cmbrsga0s9bx.me-central-1.rds.amazonaws.com",
    port="3306",
    user="cilantro",
    password="LSQiM7hoW7A3N7",
    database="cilantrodb"
    )
    mycursor = mydb.cursor()

    mydb2 = mysql.connector.connect(
    host="68.183.76.41",
    port="40601",
    user="cilantro_readonly",
    password="{2O7EAhSj>[Ksu^+bAcR",
    database="cilantro"
    )
    mycursor2 = mydb2.cursor()

    mycursor.execute(QUERY_1)
    result = mycursor.fetchall()
    promos_app = [row[0].lower() for row in result]
    mycursor2.execute(QUERY_2)
    result = mycursor2.fetchall()
    promos_oppe = [row[0].lower() for row in result]

    if name not in promos_oppe and name not in promos_app:
        return name
    else:
        count = 1
        new_name = name + str(count)
        while new_name in promos_oppe or new_name in promos_app:
            count += 1
            new_name = name + str(count)
        return new_name

def create_promocode_oppe(promocode_names):
    print(f'Creating OPPE {promocode_names[0]}')
    session = requests.session()

    # Print statement to check if the login page is successfully fetched
    page = session.get(url=CIL_LOGIN_URL_OPPE, headers=HEADER_OPPE)

    cookies = session.cookies

    soup = BeautifulSoup(page.content, features="lxml")
    token = soup.find(attrs={"name": "_token"})['value']
    payload = {
        "email": CIL_EMAIL_OPPE,
        "password": CIL_PASSWORD_OPPE,
        "_token": token
    }

    # Print statement to check if the login is successful
    login = session.post(url=CIL_LOGIN_URL_OPPE, data=payload, headers=HEADER_OPPE)
    # Check if there's any error during login
    if "Invalid email or password" in login.text:
        print("Error: Invalid email or password.")
        return

    # Print statement to check if the promo page is successfully fetched
    create = session.get(url=CIL_PROMO_URL_OPPE, headers=HEADER_OPPE)
    soup = BeautifulSoup(create.content, features="lxml")
    token = soup.find(attrs={"name": "_token"})['value']

    for promocode_name in promocode_names:
        payload = {
            "_token": token,
            "code": promocode_name,
            "code_type": "discount",
            "max_redeems": 3,
            "max_redeems_per_user": 2,
            "percentage": 20,
            "type": "product_branch",
            "productsIds[]": [1
,
3
,
5
,
7
,
8
,
9
,
10
,
12
,
13
,
14
,
15
,
16
,
17
,
18
,
19
,
20
,
21
,
22
,
23
,
24
,
25
,
26
,
32
,
33
,
34
,
35
,
37
,
38
,
39
,
40
,
41
,
42
,
44
,
45
,
46
,
47
,
48
,
49
,
50
,
51
,
52
,
54
,
55
,
56
,
57
,
58
,
59
,
60
,
61
,
62
,
63
,
64
,
65
,
66
,
67
,
68
,
69
,
71
,
72
,
73
,
74
,
75
,
76
,
77
,
78
,
79
,
80
,
81
,
82
,
85
,
86
,
87
,
88
,
89
,
90
,
91
,
92
,
93
,
94
,
95
,
96
,
97
,
98
,
99
,
100
,
101
,
102
,
103
,
104
,
105
,
106
,
107
,
108
,
109
,
110
,
111
,
112
,
113
,
114
,
115
,
116
,
117
,
118
,
119
,
120
,
121
,
122
,
124
,
125
,
126
,
127
,
128
,
145
,
149
,
151
,
156
,
160
,
170
,
173
,
174
,
175
,
177
,
180
,
183
,
184
,
185
,
186
,
187
,
188
,
189
,
190
,
191
,
200
,
201
,
202
,
203
,
204
,
205
,
206
,
207
,
208
,
209
,
210
,
211
,
212
,
213
,
214
,
217
,
219
,
223
,
224
,
225
,
274
,
275
,
280
,
283
,
285
,
286
,
288
,
289
,
290
,
291
,
292
,
293
,
294
,
295
,
296
,
298
,
299
,
300
,
301
,
303
,
304
,
305
,
306
,
307
,
308
,
309
,
310
,
312
,
316
,
317
,
318
,
325
,
335
,
338
,
341
,
342
,
343
,
344
,
345
,
346
,
347
,
348
,
349
,
350
,
351
,
352
,
353
,
354
,
355
,
356
,
357
,
358
,
359
,
360
,
361
,
362
,
363
,
364
,
373
,
374
,
375
,
376
,
377
,
378
,
379
,
380
,
381
,
382
,
383
,
384
,
385
,
386
,
387
,
388
,
389
,
390
,
391
,
392
,
393
,
394
,
395
,
396
,
397
,
398
,
399
,
400
,
401
,
408
,
409
,
410
,
411
,
412
,
413
,
414
,
415
,
416
,
417
,
418
,
419
,
420
,
421
,
422
,
423
,
424
,
425
,
426
,
427
,
428
,
429
,
430
,
431
,
432
,
433
,
434
,
435
,
436
,
437
,
438
,
439
,
440
,
441
,
442
,
443
,
444
,
445
,
446
,
447
,
448
,
449
,
450
,
451
,
452
,
453
,
454
,
455
,
456
,
457
,
458
,
459
,
460
,
461
,
462
,
463
,
464
,
465
,
466
,
467
,
468
,
469
,
470
,
471
,
472
,
473
,
474
,
475
,
476
,
477
,
478
,
479
,
480
,
481
,
482
,
483
,
484
,
485
,
486
,
487
,
488
,
489
,
490
,
491
,
492
,
493
,
494
,
495
,
496
,
497
,
498
,
499
,
500
,
501
,
502
,
503
,
504
,
505
,
506
,
507
,
508
,
509
,
510
,
514
,
515
,
516
,
517
,
518
,
519
,
520
,
521
,
522
,
523
,
524
,
525
,
526
,
527
,
529
,
530
,
531
,
533
,
534
,
536
,
537
,
538
,
539
,
540
,
541
,
543
,
544
,
545
,
546
,
547
,
548
,
549
,
550
,
551
,
552
,
553
,
554
,
555
,
556
,
557
,
558
,
559
,
560
,
561
,
562
,
563
,
564
,
565
,
570
,
571
,
572
,
573
,
574
,
575
,
576
,
578
,
579
,
580
,
581
,
582
,
583
,
584
,
585
,
586
,
587
,
588
,
589
,
590
,
591
,
592
,
593
,
594
,
595
,
596
,
597
,
598
,
599
,
600
,
601
,
602
,
603
,
604
,
605
,
606
,
607
,
608
,
610
,
611
,
612
,
613
,
614
,
615
,
616
,
617
,
619
,
620
,
621
,
622
,
623
,
624
,
625
,
626
,
627
,
628
,
629
,
630
,
631
,
632
,
633
,
634
,
636
,
637
,
639
,
640
,
641
,
642
,
643
,
644
,
645
,
646
,
652
,
653
,
654
,
655
,
656
,
657

],
            "branchesIds[]": [2,4,5,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,33,
                            34,36,38,39,41,42,44,45,46,47,48,52,53,54,55,59,60,61,65,66,69,71,72,73,74,
                            75,76,78,80,83,86,87,88,89,90,91,92,93,94,95,96,97,98],
            "order_min_amount": 40,
            "starts_at": datetime.now(pytz.utc).astimezone(pytz.timezone('Etc/GMT-2')).strftime("%Y-%m-%dT%H:%M"),
            "expires_at": "2024-04-15T23:59",
            "first_order": 0,
            "is_active": 1
        }
        response = session.post(url=CIL_PROMO_URL_OPPE, data=payload, headers=HEADER_OPPE)
        if response.status_code != 200:
          print(f"Server Error: {response.status_code} - {response.text}")
        print(f"Promocode {promocode_name} created on OPPE backend.")
        # time.sleep(2)
def create_promocode_app(promocode_names):
    print(f'Creating APP {promocode_names[0]}')
    session = requests.session()

    # Fetch login page
    login_page = session.get(url=CIL_LOGIN_URL_APP, headers=HEADER_APP)

    # Prepare payload for login
    payload = {
    "email": CIL_EMAIL_APP,
    "password": CIL_PASSWORD_APP,
    "timezone": "Africa/Cairo"
    }

    # Perform login
    login = session.post(url=CIL_LOGIN_URL_APP, data=payload, headers=HEADER_APP)

    # Check if login is successful
    if "Invalid email or password" in login.text:
        print("Error: Invalid email or password.")
        return

    # Fetch promo page
    # print("Fetching promo page...")
    # promo_page = session.get(url=CIL_PROMO_URL, headers=HEADER)
    # print("Promo page fetched successfully.")

    for promocode_name in promocode_names:
        payload = {
          "title":
          f"Mother's Day Campaign",
          "promocode":
          promocode_name,
          "vendor_id[]": [13, 12, 23, 24, 22, 20, 17],
          "category_id[]": [1,2,3,10,11],
          "products_id[]": [231,131,212,232,130,233,23,88,86,118,71,76,117,62,217,216,38,29,25,31,83,18,82,
          213,70,73,168,167,166,162,5,68,49,78,77,75,132,128,80,89,107,22,126,84,215,125,124,110,112,59,
          172,171,91,180,179,85,39,28,123,24,165,42,102,122,210,163,96,11,135,27,41,33,30,40,149,248,36,
          55,53,45,66,50,44,48,143,94,181,65,69,164,92,113,72,54,98,139,138,67,64,81,95,155,142,101,87,109,
          105,97,136,100,99,106,116,114,60,161,159,160,154,111,127,141,144,35,242,244,240,241,243,170,249,
          93,46,140,115,79,104,90,214,156,250,51,219,108,103,57,63,56,32,34,134,133,47,74,52,150,148],
          "subcategory_id[]":
          [
          9, 13, 32, 29, 7, 21, 25, 8, 18, 20, 4, 1, 3, 5, 6, 19, 30, 26, 22, 11, 10, 12, 2, 14, 23, 31
          ],
          "minimum_order_amount":
          40,
          "maximum_order_amount":
          10000,
          "maxusage":
          1,
          "peruser_usage":
          1,
          "start_datetime":
          datetime.now(pytz.utc).astimezone(pytz.timezone('Etc/GMT-2')).strftime("%Y-%m-%dT%H:%M"),
          "end_datetime":
          "2024-04-15T23:59",
          "amount":
          20,
          "promocodetype":
          "Percentage",
          "status":
          "Active",
          "description":
          "This is an automated promocode created for the mother's day campaign"
        }
        # Post to the promo code creation endpoint
        create_promo = session.post(url=CIL_PROMO_URL_APP,
                                    data=payload,
                                    headers=HEADER_APP)

        # Check for errors in the response
        if create_promo.status_code != 200:
          print(f"Error creating promocode {promocode_name}: {create_promo.text}")
        else:
          print(f"Promocode {promocode_name} created successfully on App backend.")
        time.sleep(2)

for i,name in enumerate(worksheet.col_values(2)[1:], start=2):
    if worksheet.cell(i, 3).value == None :
        new_promo = generate_promo(name.lower())
        create_promocode_oppe([new_promo])
        create_promocode_app([new_promo])
        worksheet.update_cell(i, 3, new_promo)
        time.sleep(5)
        print('-----------------')
    else:
        pass
print("Done :)")



