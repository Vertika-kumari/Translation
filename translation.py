##DNA to RNA translation

def transcription (rna_seq):


    codons_dict = {
    'UUU' : 'F',
    'UUC' : 'F',
    'UUA' : 'L',
    'UUG' : 'L',
    'CUU' : 'L',
    'CUC' : 'L',
    'CUA' : 'L',
    'CUG' : 'L',
    'AUU' : 'I',
    'AUC' : 'I',
    'AUA' : 'I',
    'AUG' : 'M',
    'GUU' : 'V',
    'GUC' : 'V',
    'GUA' : 'V',
    'GUG' : 'V',
    
    'UCU' : 'S',
    'UCC' : 'S',
    'UCA' : 'S',
    'UCG' : 'S',
    'CCU' : 'P',
    'CCC' : 'P',
    'CCA' : 'P',
    'CCG' : 'P',
    'ACU' : 'T',
    'ACC' : 'T',
    'ACA' : 'T',
    'ACG' : 'T',
    'GCU' : 'A',
    'GCC' : 'A',
    'GCA' : 'A',
    'GCG' : 'A',
    
    'UAU' : 'Y',
    'UAC' : 'Y',
    'UAA' : '*',
    'UAG' : '*',
    'CAU' : 'H',
    'CAC' : 'H',
    'CAA' : 'Q',
    'CAG' : 'Q',
    'AAU' : 'N',
    'AAC' : 'N',
    'AAA' : 'K',
    'AAG' : 'K',
    'GAU' : 'D',
    'GAC' : 'D',
    'GAA' : 'E',
    'GAG' : 'E',
    
    'UGU' : 'C',
    'UGC' : 'C',
    'UGA' : '*',
    'UGG' : 'W',
    'CGU' : 'R',
    'CGC' : 'R',
    'CGA' : 'R',
    'CGG' : 'R',
    'AGU' : 'S',
    'AGC' : 'S',
    'AGA' : 'R',
    'AGG' : 'R',
    'GGU' : 'G',
    'GGA' : 'G',
    'GGC' : 'G',
    'GGG' : 'G',
    }

    protein = ""
    for i in range(0, len(rna_seq), 3):
        codon = rna_seq[i:i+3]
        amino_acid = codons_dict.get(codon, '')
##        if amino_acid == '*':
##            break to stop translation
        protein += amino_acid
    return(protein)

##front end command

input_rna = str(input("feed RNA seq in CAPITAL fonts: "))
output_prot = transcription (input_rna)
print(output_prot)



























    
    
