import requests
import json
import csv

url = "https://retr.app/LoanOfficer/GetLOsByBranch"

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "connection": "keep-alive",
    "content-length": "23",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "cookie": "uwguid=WEBLS-26f71bc4-b4aa-4b08-8827-1ffeb78b9d9d; ai_user=D4y+SGZLEVB0tGjCEkXXII|2025-07-03T16:34:14.222Z; _ga=GA1.1.417251509.1751560457; hubspotutk=43c5f7811328349c527c74b9665474af; _lc2_fpi=a0fe120aae25--01jz8j752bee756qjtqk9w4brz; _li_ss=CgA; .AspNetCore.Cookies=chunks-2; messagesUtk=c4b4b2ee6b9540ad90c9920087395861; __stripe_mid=5d8abc45-e063-4f84-b504-446982567980779aa4; ARRAffinity=f9b40ae4b4ae41a96abe95094c273645c386d1a0ba45880f13d7843839a7cfa0; ARRAffinitySameSite=f9b40ae4b4ae41a96abe95094c273645c386d1a0ba45880f13d7843839a7cfa0; .AspNetCore.Antiforgery.cdV5uW_Ejgc=CfDJ8FeMfPkJZi1MmiJJhiNJXXnap58B9tCVQOj3OqqChYwV-FNlMhjy3NKl8IsbuUJRc4DjhmHBeAznV2gcij1EfrSK7G-tPZsj5MdjTlZRUWPYnEI8cGgtCjBokNv3zddujw4pAKYD5Ben8S13NThqq0o; __hssrc=1; .AspNetCore.CookiesC1=CfDJ8FeMfPkJZi1MmiJJhiNJXXnJ1xc84cbLJefEK7G97Qu8Acm24EJr8x0elnoc3CFTWIyAPKxTIJ6hTS8UhIB4SJPZmgVrJicbkU7f9jGnFDVk4tyQI5JOf9fgFSoQV96onms_bwuGQAzGW3f3GeX_L5DZz9CMMM5xfLgJrsw_Yap97-kDw4Q6CaE3dJdWoCBcta2gtKwnYyLAWDAlpt2CZsd_btghgmnY768rrPzFSC_mNZ2h8FZVomDbVJs2XPyT3rbEBf-Sk9vCg7pvHyQCtlvucuz7-2AZeQhM3dTUU29LffhI2bf7WDFB6qXpFakba6j1eh8Iubr2_0eerzmu2RlI82ZgOLcXwPDEY-daFPQCQEa0v1rTL7M17cX7eocxy07KdsFsa48sHKWbrsy4g_knVVqyq3HG8yzQNTu_NGAryV0NY4oUS8QtRmixWMkHRVYoIe-p7NFpuSixGo1bxohbYZ6jT0UMwaWYNnT7mkMnk5eX1XF7e8GIZbw9XgpVMd9-dB2wmHQb4WG0CosCJASBEuz31qEYCMNjpKRKc8KSDHDMxirNhPPzebf92Afy4I57WswyMcipWzTwa2me-710TK7dU_PeLb00ftxPD0CxNKLyZkZTGRomCg1CjhrjskTpBbzIVm_kSmE1rH_d4XbD4PWxMgBSHDyPBxtjaSUYZqLc20PPHnw074X2wn82mEkpUXU5_88RGvLZ5CT4i2BN9MBEbbEWHCQb5qijnQBPs5eLeW91Hm8t86tE7HKcX8vnFBBlhl7MnWKp195SfdLbNnYq--5cs95nd1k-1hRvxAAzb76k2uZ14aHVUkncqJumrA6mfnnhOo2uBl9wFaBBWJrUAwS-prYK5EYTeuAaAH0ZfCax7CQROjkeBtt24EiovPXIpPm8mVfHgZ7Osn5FBbQcqVBWg5Wz_m0Y0zrG6gk9s2JIOWTqigFkdzOksP7RB_QQlgJWR9WUYcqthLHf75I_EFhY1nBwa8_i8ahDzbsACPJHzX7QMZAQrDzmNuB_5dJpVy1sbqhNUpYAETm8FjGQSRmx7gYysMKMloa4lD9Jh-CJEGdjFwpKi4NvDaYSnqCGBWKsswTZ4eqC1tnItf2dD2gWzjNCXn_kdJ7p4kDq763nbcdI6VxcnmyYjd8VAZ9uDU4Wz68TbIkQMVjCtk6airUfM61D3Ijv5-7R4FRXNPU_KTtsdyqXHpwrBVRoZfqjV6XousxgDPS_lCHNOy_wvqoyuU_VpTIK9wPePaFvnzeONsQqOM6zroUYLwy5Zn48H8KV3aZMKe5FNXXk7CZG7GEfVggzTbd8ZFzhgMxxEgVYXQNPpJe4sfc07fr-XR4tTFwlWXE9e4dIyTa5-4tHSuEKWIML20zFbqgdd-3vNdE0y07w_QiUsaWNbPcykSWgvClOd2CPUGzFk1qDUk_esVzzU7ij6UZi-0cRqgn6K39IUxabShdcvpR0VzpbAcJp0Pp_-nLMAEaZwi4ozX7D0nCCLSaPHzrHWCYL6jin6yrDQpjlyvIJbRjR2yHsvCOViG1Yhwr00214FKBAOLwZv8ldY4H30YzkgRvGLp2VskqB7164dGoY0V6uBLwgAzjBRShOvTnr4Ua7gcZUx46r5xVygOjQr5SbqOHkkw1jG6m4OrnQp_QfROfTzN-beuXSzzjb3KBVbQWkRA4hrikCJbAJ9qsPGEpbsU0i2STygzHJaI7CT6o_tHYNdoodSOcdNNldozxaGesXCCo_vvbZ3VGfgD251Of0FP7h-ydXOvJQcJ_I-7ROTlmSnPtGCGrr31tlzZGrbFhZ8BrdI-kpPPgL4z-MhQZBPjedF_gYhkyFJO60xe1kwSrJKRNhNC5cw7iPf0-UXhhO1yTzHS8gYZtaliJ4ej1LWsnkjTSj8jk1Cr63Nma1yFAqNsFERo0H5whu6AuS8uq7kHoXr6fOQ5-bCAnJU07h_LAAImXH-kn7kXO0r2ZNlPul56x1DnaeEwIIMaeKMPilLYdFGtLOXaO6IZP6HrNKgz03ra0FkmZGK8Tg6Y1-GdDILBuSGyXnTYBsq-cxgtJGpNvfEu34KN-P9EzcvL8qJosy2ForqvdTtRC-E2mOMJs7h_B0cWk6KVYrAqTDPtmpUEaenux5W22byajXs_L9EoKXLBoAOnvrobx86ZiTBtF3mh_yva6uh1TPgGCp9HV3rsgyO5-2qe0iKO8IzjVkKuDsHVTyhvrhBK2fmsXubNNX_yab4yjGceBef7pcrb9oZcrqRlu7o081_XcnzK78qN04DtUbfGyGjxhU-NNyROx4h_2UhoUOQE2mHLWh98c685Ay65_to1TNGxJz_-Kp_H-ERVEPfvd5SVc6vDkkER48LrT8QyDMB04biCt4MhqbSZwWINxFnQJik0EmoRz9JcoKMGxH7mBvJYvdXVcaZLorxP6osIRdvma7hI3a3KI-4Slj0SgDdYlztP1ZI-njvmz5KkN8F2X3F8ckD8yuWRuT-SrPtMJJsrxtmn_6jOe9wqMKCytEXpbwG49Ryiwg-8npUPqQaJ15shTZI9c1-7ihH55sA-q9S2ljdy_tnv7gjcZC6wCnde4-wUAODZmYnmJmBdnW2E7tFCKK-Gc6F_5ol0OPcJG99r4gi_KOleb93XUyuWEdzZKoEx4yAgmsRKc-Zxqn0N8uIo3uXeaSM7Ad3pbJps8iL1XyWAF_CKB7hPek94jwRYtHyM5ey87Kh0XqJhWxIt2Cm_RCmVNnF9OLC33T3H_3VPD51PxNBKz7GXRqxzbHSm1XUgrnEnPXUeCxG6Z0VygaQ-Q-V0UzXiIC67tlnUygViTSBkkFFSyFbCtP_264Re6hXj6phmNVOFFybVWbhlVhAIxSCOeym0Z2cvmaHIhMXVutp78Lzck7yJBLSvn2aM_bODFoLT5Pf22dFPA6UbH8OoUSB6KJ8zMIisoJPXiNUP9SjFNxSF7xbWhInyRFKWiTTkGuha1LRGsbNpZMFtKCkdeeekWZ8QM1UDoeGrUhhvVmL59vZuFM33OlMJSTC09KWr4J9Dck3WG2mXyts4ngz4vq-NjxWcuzqJfhyJby_-p9OanDYagcgvt2N5vXYbyy5au3A36OxfHU7fLBnT0F02MqhL7CEMY8-J4r-pX9f-fOm8I0cUrWKqVfe0Jwdayts6noiR0Kp9hlmGev4RAQBpaIeoTdSf7HQCXmG0h1FZziLgQPcXesFuDQk91Jam3WzZioffYGs_vZ3HKg1trvaFd9VDNFPqkddnJf-njwzWW2JpPHquSa3Bsot4y_sp5XJFDvf_Nzq8AlS3uTLF6bTCi76GwdhjO_ICNaSBrURCiDETpWDMDr-c_go3_5gYh1MUX55DnBLNf-NP9B0RwdNhrvGpm888R3tRdN3VQdcQTabRGAgPJqKJW9FE2e4xzKr3xwMa8LwZ9ZN4d9k6qybAx6XMyMnSu_Pq7eozYCLD-IaAXm59L6OxgCVplq8cjZXVq5pOeTmqxQsFV4RApKpQljjBpCQcyiqZazUnOXHSw9FVRgKHdPs_7cRFt36T91OC8xyKm_JRLzMI6u2w2_ekRYjElcT7bsq4nDxYztF93AfIuQkPVm_BdnsnoApB_S96_j2x206d0L1hURNJoYww5_ZeSQnZ7RqUTHHMtCuQMD6OXewCrAqAQ3i4nR_FArqpRqr_IHAXQzQ_E-w_3A0mnHYy3_TSuViaxVLcV-MF3kzD8PGaG1dWKsnjbVxByL2ilNwejoSQX_OIpjRzofTDT60oF1JyKkSjAATua_0jxSQnFAdDGzXffIbRTh6v5ZbF7YTmLv1MTEOmQhHWebV7SNMo2bevWDGfVXbry-wyNCzx7aO_Wj-uD2pKp_02h8DRDMlkiLFtjsR48Sik7mdvQkAm7afiH1Y4nuMabHSwS6taCM0aufCI; .AspNetCore.CookiesC2=sE8RlnFCTUruBQVki4BKBogVjHFnkFS3M0f7cnZcxMtF4AAQSuN0QjWaKtbeFckAFrP4p4_y0VKuqHnmvWWKg1M5y_vu2XrDz_6nQ4FPBs_M2t5Zlx9cw3zJxbAptQ9idlLyTTWpMq0GV7yM-RZWrj1ZnY5N7yprROtXsznZ4oE6WHxXGIHIiisleEKSb4VvuONFTKgRRQSlskOblXV0e6OmAsfauAqOiUdNkleGMVMSvlcOXG-L1Jke6IAGM_ftg20LBFWV1DTDAXPI84Y5FdTMoEYvEPDLwYjjxeAAdn-KysPzYxbN077qkavOUkzYS_lY0jqsKU9rJL0GYiwW01RZiHKl89jStea2yENnT3U7Vm456chgZBaBlBN-RpReCW6ubNnB6-UqCO-3GpITt6MtmLGIDAAMY7Z3D7OxoYF9iCKZx8OZneRmLvp5H6VlURFCqsX_r7bxHI01TrUvZSymlENfFXSahf5brYBI8xfpnb61QpTfebDJS98zTPrA1eyLbZHegYkHgZJ1sjsVFHfFdgtr1syM9H6qOfu5hg08IlHlJynY2qCVblbv3mS2nEUymEm33iEULHc8gFOZ39ug0L1FHZtKt4XKNcwKM6BmR2pilXOXaSt_A5qjI6ZhcuDPK4Sslo8XShEOhfTeI-FmZ53JYitQfLQvZOBAe8fplPf83WgQfFyWkVvZA--obDHF_s9pBRHUNJ6BKlPrKSo-UcE1DBJgiffl4513Ru9McJ2_MAThv8Pf_XdHhY2YEPKLzOMYq92y0M0PSA14D1bT3FXupyJKqvC6KNWL93vEfveffojmZr9o0FLuMkDZ_K-SpOGYyvcYdaMfnkaTW7Ig5FRrNlhVzigBFLKFR66dV_qFQlMNZ-qaxY-blSkSCoRYAX3ynEIGZ2NOeu5qm59MymkzbIImKYbsXNvDJvq7xhwMlBu7om-1jbSO9X5Qr6MhsV5UgOPvZ5ofhGcGOhWIuFBp-nfKAlU5TtM5kP-GkzgS8fkTU-NQ3qChbMQXCFwysDi_8gvekz9RrP_yHoC57xZannf9CVB-UKEcpZ7nn_Mv123x0_C5TZqIfyCo8; nologo=0; hubClock=1; hubEmail=apitterman@nightowl.consulting; hubToken=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhcGl0dGVybWFuQG5pZ2h0b3dsLmNvbnN1bHRpbmciLCJhdWQiOiI0NDEyNjU5MCIsImxhc3RfbmFtZSI6IlBpdHRlcm1hbiIsImV4cCI6MTc1MTk1MTQ5NSwiaWF0IjoxNzUxOTA4Mjk1LCJmaXJzdF9uYW1lIjoiQWFyb24ifQ.hIBiCGt240dpyEGtWaauEMNlk1b6t4Zqb_CP-A1ZlO8; hubUser=6525; hubName=Aaron%20Pitterman; upolloLogin=0; __hstc=16353321.43c5f7811328349c527c74b9665474af.1751560458287.1751914628339.1751918663392.7; hShareChecks=0; ai_session=69pvzkw2GDKlNzwP2dc6tT|1751914054963|1751919913618; __hssc=16353321.2.1751918663392; TawkConnectionTime=0; twk_uuid_642f9b8231ebfa0fe7f6f6b3=%7B%22uuid%22%3A%221.6AsAA82D4t3X1TbCQmLcTS3iJQnVP4ivamVHDKLpoVXPetxaqgEEjPYclt0EWuDBFgzWGgtC1zmgvR9ftXveBi1sPBb5IALE8XhYJi6Xs3ldWZBj%22%2C%22version%22%3A3%2C%22domain%22%3A%22retr.app%22%2C%22ts%22%3A1751919918168%7D; __stripe_sid=a7a71043-b2d8-4dfd-877d-3d26486bd3316dade7; _ga_R1JEDY5P0G=GS2.1.s1751914584$o7$g1$t1751919942$j28$l0$h0",
    "host": "retr.app",
    "origin": "https://retr.app",
    "pragma": "no-cache",
    "referer": "https://retr.app/LoanOfficer/FindByCompany",
    "sec-ch-ua": '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}

# Send payload as URL-encoded string
payload = "term=NFM%20lending&state="

response = requests.post(url, headers=headers, data=payload)

print(response.status_code)
print(response.headers)
print(response.text)

try:
    data = response.json()
    print(json.dumps(data, indent=2))
    # Save to CSV
    if "data" in data and isinstance(data["data"], list) and data["data"]:
        # Flatten LoanVolume for all rows first
        flat_rows = []
        for row in data["data"]:
            row = row.copy()  # avoid mutating original
            if "LoanVolume" in row and isinstance(row["LoanVolume"], dict):
                row["LoanVolume_display"] = row["LoanVolume"].get("display", "")
                row["LoanVolume_raw"] = row["LoanVolume"].get("raw", "")
                del row["LoanVolume"]
            flat_rows.append(row)
        keys = list(flat_rows[0].keys())
        with open("branches.csv", "w", newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            for row in flat_rows:
                writer.writerow(row)
        print("Saved data to branches.csv")
    else:
        print("No data to save.")
except Exception as e:
    print("Failed to parse JSON response:", e)
    print(response.text)