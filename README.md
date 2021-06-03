# ქვიზი4 #



### *აღწერა* ###

* q4 მოდულში დაწერილ პროგრამას საიტიდან მოაქვს ინფორმაცია ვაკანსიებზე *
* [ვებგვერდი](https://www.timesjobs.com/candidate/job-search.html?from=submit&searchType=Home_Search&luceneResultSize=25&postWeek=60&cboPresFuncArea=35&pDate=Y&sequence=1startPage=1)

* გამოყენებულია *requests*, *bs4*, *sqlite3* მოდულები
BeautifulSoup-ის გამოყენებით get request-ით მიღებულ საიტიდან წამოღებულ ინფორმაციას ვამატებ მონაცემთა ბაზაში.
```bash
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
```

* სხვა გვერდებიდან ინფრომაციის წამოღებისთვის,URL ში page პარამეტრს ციკლის საშუალებით ყოველ 15 წამში გადავცემ მთელ რიცხვებს და ახლიდან ვგზავნი get request-ს
```bash
for num in range(1, 6):
url = f'https://www.timesjobs.com/candidate/job-search.html?from=submit&searchType=Home_Search&luceneResultSize=25&postWeek=60&cboPresFuncArea=35&pDate=Y&sequence={i}&startPage=1'
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
```
