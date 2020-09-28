# itp_test
test
Here are the data you should work with (Name/Email/Phone). All phones are stored as 10 digits - no brackets, spaces or dashes:

CONTACTS:

Alice Brown / None / 1231112223
Bob Crown / bob@crowns.com / None
Carlos Drew / carl@drewess.com / 3453334445
Doug Emerty / None / 4564445556
Egan Fair / eg@fairness.com / 5675556667



LEADS:

None / kevin@keith.com / None
Lucy / lucy@liu.com / 3210001112
Mary Middle / mary@middle.com / 3331112223
None / None / 4442223334
None / ole@olson.com / None



REGISTRANTS (these should be read as JSON mentioned above)

Lucy Liu / lucy@liu.com / None
Doug / doug@emmy.com / 4564445556
Uma Thurman / uma@thurs.com / None



Now what you should do:

We believe that only real people will register for our webinar. So as mentioned, we want to make sure that all registrants will end up in our Contacts. If they provide us with more details than we currently have (like phone or email) - great! We should store them as well. But non-empty values in Contacts should not be updated.



In order to match our registrants, we should follow this order:

1) Try to match registrant's email to our Contacts list

2) If not matched, try to match registrant's phone to our Contacts list

3) Otherwise try to match our LeadsList with email (if Lead is matched, remove it from LeadsList and add to ContactsList)

4) Else match our Leads with phone (same rule as above applies)

5) If not matched, simply add it to ContactsList
