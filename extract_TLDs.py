namecheap_html = open('domains.html','r')
TLDs = []

for input_string in namecheap_html:
    start_index = 0
    while True:
        start_index = input_string.find("class=gb-tld-name>", start_index)
        if start_index == -1:
            break
        end_index = input_string.find("<", start_index)
        substring = input_string[(start_index+18):end_index]
        TLDs.append(substring)
        start_index = end_index
namecheap_html.close()

tlds_json = open("TLDs.json", "w")
tlds_json.write('[')

for TLD in TLDs:
    if TLD == TLDs[-1]:
        tlds_json.write('"'+TLD+'"')
    else:
        tlds_json.write('"'+TLD+'",')
tlds_json.write(']')
tlds_json.close()

