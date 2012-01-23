from lxml.html import parse

class Speaker(object):
    def __init__(self, name, bio, gender):
        self.name = name
        self.bio = bio
        self.gender = gender

def parse_oscon(url):
    year_parser = {'conferences.oreillynet.com/pub/w/58/speakers.html':parse_oscon_2007}
    parser = parse_oscon_default
    for year in year_parser:
        if year in url:
            parser = year_parser[year]
            break

    doc = parse(url).getroot()
    return parser(doc)


def parse_oscon_default(doc):
    speakers = []
    for speaker_div in doc.cssselect("div.en_speaker"):
        name = speaker_div.cssselect("div.en_speaker_details a")[0].text_content().strip()
        bio = []
        for bio_paragraph in speaker_div.cssselect("div.en_speaker_bio p"):
            bio.append(bio_paragraph.text_content())
        speakers.append(Speaker(name, "\n".join(bio), "unknown"))
    return speakers

def parse_oscon_2007(doc):
    doc.make_links_absolute()
    speakers = []
    for speaker_div in doc.cssselect("div.speaker-blurb"):
        name = speaker_div.cssselect("h3")[0].text_content().strip()
        print "Getting", name
        links = speaker_div.cssselect("a")
        for link in links:
            href = link.get("href")
            if href and "e_spkr" in href:
                speaker_doc = parse(link.get("href")).getroot()
                bio = []
                for bio_elem in speaker_doc.cssselect("div.bio"):
                    bio.append(bio_elem.text_content().strip())
                bio = "\n".join(bio)
        speakers.append(Speaker(name, bio, "unknown"))
    return speakers

def make_find_word_fcn(word):
    return re.compile
