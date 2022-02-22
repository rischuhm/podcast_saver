from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://www.rbb-online.de/rbbkultur/podcasts/marcel-proust/auf-der-suche-nach-der-verlorenen-zeit-podcast.html')

links = r.html.find('.doctypeaudio')

print(f"Found {len(links)} files to download\n")

for link in links:
    name= link.find(".manualteasertitle", first=True).text.replace(":","_").replace("/","_")
    print(f"Downloading {name}", end="\t")
    mp3_link = list(link.find(".ico_download", first=True).links)[0]
    open(f'{name}.mp3', 'wb+').write(session.get(mp3_link).content)
    print("🗸")

 
print("\n\nFINISHED")
