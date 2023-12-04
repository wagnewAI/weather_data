from requests_html import HTMLSession
s = HTMLSession()
query = 'addis ababa'    #str(input("enter city name = "))
url = f"https://search.yahoo.com/search;_ylt=AwrFGC0gkG1ldFk9g_FXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA3locy1pbnZhbGlkBGZyMgNzYi10b3AEZ3ByaWQDVzk0WUdSbXdSamk4cXVUbk15REFVQQRuX3JzbHQDMARuX3N1Z2cDOQRvcmlnaW4Dc2VhcmNoLnlhaG9vLmNvbQRwb3MDMARwcXN0cgMEcHFzdHJsAzAEcXN0cmwDMTYEcXVlcnkDd2VhdGhlciUyMGV0aGlvcGlhBHRfc3RtcAMxNzAxNjc5MTQx?p=weather+{query}&fr2=sb-top&fr=yhs-invalid"
r = s.get(url, headers = {"user_agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'})
temp = r.html.find('div.imperial-metric.fz-50.lh-40.pr-2', first=True).text
unit = r.html.find('button.degree-unit-button.fz-16.bgc-none.bd-0.p-0.cur-p', first=True).text

desc = r.html.find('p.fz-14.lh-20.fc-charcoal.pt-1',first=True).text
print(query,temp, unit, desc)
