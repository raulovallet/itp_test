# Here are the data you should work with (Name/Email/Phone). All phones are stored as 10 digits - no brackets, spaces or dashes:
#
# CONTACTS:
#
# Alice Brown / None / 1231112223
# Bob Crown / bob@crowns.com / None
# Carlos Drew / carl@drewess.com / 3453334445
# Doug Emerty / None / 4564445556
# Egan Fair / eg@fairness.com / 5675556667
#
#
#
# LEADS:
#
# None / kevin@keith.com / None
# Lucy / lucy@liu.com / 3210001112
# Mary Middle / mary@middle.com / 3331112223
# None / None / 4442223334
# None / ole@olson.com / None
#
#
#
# REGISTRANTS (these should be read as JSON mentioned above)
#
# Lucy Liu / lucy@liu.com / None
# Doug / doug@emmy.com / 4564445556
# Uma Thurman / uma@thurs.com / None
#
#
#
# Now what you should do:
#
# We believe that only real people will register for our webinar. So as mentioned, we want to make sure that all registrants will end up in our Contacts. If they provide us with more details than we currently have (like phone or email) - great! We should store them as well. But non-empty values in Contacts should not be updated.
#
#
#
# In order to match our registrants, we should follow this order:
#
# 1) Try to match registrant's email to our Contacts list
#
# 2) If not matched, try to match registrant's phone to our Contacts list
#
# 3) Otherwise try to match our LeadsList with email (if Lead is matched, remove it from LeadsList and add to ContactsList)
#
# 4) Else match our Leads with phone (same rule as above applies)
#
# 5) If not matched, simply add it to ContactsList
import json
import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

ContactList = [
    'Alice Brown / None / 1231112223'.split(' / '),
    'Bob Crown / bob@crowns.com / None'.split(' / '),
    'Carlos Drew / carl@drewess.com / 3453334445'.split(' / '),
    'Doug Emerty / None / 4564445556'.split(' / '),
    'Egan Fair / eg@fairness.com / 5675556667'.split(' / '),
]
LeadsList = [
    'None / kevin@keith.com / None'.split(' / '),
    'Lucy / lucy@liu.com / 3210001112'.split(' / '),
    'Mary Middle / mary@middle.com / 3331112223'.split(' / '),
    'None / None / 4442223334'.split(' / '),
    'None / ole@olson.com / None'.split(' / '),
]

print('Contacts start:')
for contact in ContactList:
    print(contact)
print('---------------')
print('Leads start:')
for lead in LeadsList:
    print(lead)


class Contact:
    def __init__(self, idx):
        self.idx = idx
        self.Name = ContactList[idx][0]
        self.Email = ContactList[idx][1]
        self.Phone = ContactList[idx][2]

    def setName(self, Name):
        self.Name = ContactList[self.idx][0] = Name

    def setEmail(self, Email):
        self.Email = ContactList[self.idx][1] = Email

    def setPhone(self, Phone):
        self.Phone = ContactList[self.idx][2] = Phone


class Lead:
    def __init__(self, idx):
        self.idx = idx
        self.Name = LeadsList[idx][0]
        self.Email = LeadsList[idx][1]
        self.Phone = LeadsList[idx][2]

    def setName(self, Name):
        self.Name = LeadsList[self.idx][0] = Name

    def setEmail(self, Email):
        self.Email = LeadsList[self.idx][1] = Email

    def setPhone(self, Phone):
        self.Phone = LeadsList[self.idx][2] = Phone

    def transferToContact(self):
        ContactList.append(LeadsList[self.idx])
        LeadsList.pop(self.idx)


print('---------------')
print('json data:')
with open("registrants.json", "r") as registrants_file:
    start_contact = [] + ContactList
    start_leads = [] + LeadsList
    registrants = json.load(registrants_file)
    index_to_transfer = []
    for registrant in registrants['registrants']:
        print(registrant)
        idx = 'NotFound'

        for index_contact, contact in enumerate(start_contact):
            if contact[1] == registrant['email'] and registrant['email'] != 'None':
                idx = index_contact
            elif contact[2] == registrant['phone'] and registrant['phone'] != 'None':
                idx = index_contact
            else:
                idx = 'NotFound'

            if idx != 'NotFound':
                contact_obj = Contact(idx)
                if contact_obj.Name == 'None':
                    contact_obj.setName(registrant['name'])
                if contact_obj.Email == 'None' and re.search(regex, registrant['email']):
                    contact_obj.setEmail(registrant['email'])
                if contact_obj.Phone == 'None' and len(registrant['phone']) == 10 and registrant['phone'].isdigit():
                    contact_obj.setPhone(registrant['phone'])
                break
        if idx == 'NotFound':
            for index_lead, lead in enumerate(start_leads):
                if lead[1] == registrant['email'] and registrant['email'] != 'None':
                    idx = index_lead
                elif lead[2] == registrant['phone'] and registrant['phone'] != 'None':
                    idx = index_lead
                else:
                    idx = 'NotFound'

                if idx != 'NotFound':
                    lead_obj = Lead(idx)
                    if lead_obj.Name == 'None':
                        lead_obj.setName(registrant['name'])
                    if lead_obj.Email == 'None' and re.search(regex, registrant['email']):
                        lead_obj.setEmail(registrant['email'])
                    if lead_obj.Phone == 'None' and len(registrant['phone']) == 10 and registrant['phone'].isdigit():
                        lead_obj.setPhone(registrant['phone'])
                    index_to_transfer.append(idx)
                    break
        if idx == 'NotFound':
            ContactList.append([
                registrant['name'],
                registrant['email'] if re.search(regex, registrant['email']) else 'None',
                registrant['phone'] if len(registrant['phone']) == 10 and registrant['phone'].isdigit() else 'None',
            ])

for index in index_to_transfer:
    lead_obj = Lead(index)
    lead_obj.transferToContact()

print('---------------')
print('Contacts final:')
for contact in ContactList:
    print(contact)
print('---------------')
print('Leads final:')
for lead in LeadsList:
    print(lead)
