class Sequence:
    def __init__(self, string):
        self.sequence = string

    def transcribe(self):
        return 'U'.join(self.sequence.split('T'))

    def hamming_distance(self, s2):
        h = 0
        if len(s2) == len(self.sequence):
            for i in range(len(self.sequence)):
                if list(self.sequence)[i] != list(s2)[i]:
                    h += 1
            return h
        else:
            return 'Строки не совпадают по длинам'


class DNA(Sequence):
    def count_nucleotides(self):
        adenine = len(self.sequence.split('A')) - 1
        thymine = len(self.sequence.split('T')) - 1
        cytosine = len(self.sequence.split('C')) - 1
        guanine = len(self.sequence.split('G')) - 1
        return {'A': adenine, 'T': thymine, 'C': cytosine, 'G': guanine}
    

    def complement_dna(self):
        string = self.sequence
        string = 'a'.join(string.split('T'))
        string = 't'.join(string.split('A'))
        string = 'c'.join(string.split('G'))
        string = 'g'.join(string.split('C'))
        return string.upper()
    

    def hamming_distance(self, s2):
        return Sequence().hamming_distance
    

    def transcribe(self):
        return Sequence().transcribe
            

        

class RNA(Sequence):
    def transcribe(self):
        return 'T'.join(self.sequence.split('U'))
    


d = RNA('UTGGAAAAUU')
print(d.transcribe())