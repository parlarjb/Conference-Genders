import csv
import gender


class Output(object):
    def __init__(self, filename):
        if not filename.endswith(".csv"):
            filename = filename + ".csv"
        self.filename = filename
        self.f = open(self.filename, "wb")
        self.writer = csv.writer(self.f, dialect='excel')

    def store_entry(self, name, gender):
        self.writer.writerow([name.encode('utf-8'), gender])

    def close(self):
        self.f.close()


def process_unknown_speakers(speakers, output):
    total = len(speakers)
    print total, "unknown speakers"
    m = {"f":"female", "m":"male"}
    count = 1
    for s in speakers:
        print s.name
        print s.bio
        done = False
        while not done:
            gender = raw_input("Male (m) or Female (f)? (%d/%d)" % (count, total))
            if gender is "f" or gender is "m":
                done = True
                gender = m[gender]
                s.gender = gender
        output.store_entry(s.name, gender)
        count += 1

def run(filename, speakers):
    o = Output(filename)
    male, female, unknown, ambiguous = gender.classify(speakers)
    unknown = unknown + ambiguous

    for s in male + female:
        o.store_entry(s.name, s.gender)

    process_unknown_speakers(unknown, o)
    o.close()
