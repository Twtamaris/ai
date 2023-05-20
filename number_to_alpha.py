list1 = ["""580 100 007
000 500 026
002 704 003
000 001 004
100 000 000
004 200 000
000 000 608
701 003 000
005 400 900
""",


    """
001 620 057
000 000 009
040 100 000
000 060 400
030 007 065
005 000 900
000 000 600
800 003 000
004 070 021
    
"""



"""
490 032 000
000 196 400
218 040 693
180 029 060
960 000 004
074 000 820
501 084 206
800 013 900
000 000 030
""",



"""
009 000 060
000 015 040
050 080 007
800 700 200
060 008 030
974 002 005
500 070 000
008 250 403
600 040 801
""",
"""
030 002 080
706 000 000
002 700 040
020 090 400
000 000 000
010 003 050
040 005 100
000 007 600
160 300 900
""",


"""
004 700 005
020 000 084
008 000 000
203 070 000
000 548 000
600 020 000
190 000 300
000 900 020
000 005 700
"""



]


# Define the digit-to-letter mapping
digit_to_letter = {
    '0': 'z',
    '1': 'a',
    '2': 'b',
    '3': 'c',
    '4': 'd',
    '5': 'e',
    '6': 'f',
    '7': 'g',
    '8': 'h',
    '9': 'i'
}

# Replace digits with letters in each string
for i in range(len(list1)):
    list1[i] = '\n'.join(
        ''.join(digit_to_letter.get(c, c) for c in line)
        for line in list1[i].split('\n')
    )

# Print the modified list
for sudoku in list1:
    print(sudoku)
    print()
#output
    """
ehz azz zzg
zzz ezz zbf
zzb gzd zzc
zzz zza zzd
azz zzz zzz
zzd bzz zzz
zzz zzz fzh
gza zzc zzz
zze dzz izz



zza fbz zeg
zzz zzz zzi
zdz azz zzz
zzz zfz dzz
zcz zzg zfe
zze zzz izz
zzz zzz fzz
hzz zzc zzz
zzd zgz zba


diz zcb zzz
zzz aif dzz
bah zdz fic
ahz zbi zfz
ifz zzz zzd
zgd zzz hbz
eza zhd bzf
hzz zac izz
zzz zzz zcz



zzi zzz zfz
zzz zae zdz
zez zhz zzg
hzz gzz bzz
zfz zzh zcz
igd zzb zze
ezz zgz zzz
zzh bez dzc
fzz zdz hza



zcz zzb zhz
gzf zzz zzz
zzb gzz zdz
zbz ziz dzz
zzz zzz zzz
zaz zzc zez
zdz zze azz
zzz zzg fzz
afz czz izz



zzd gzz zze
zbz zzz zhd
zzh zzz zzz
bzc zgz zzz
zzz edh zzz
fzz zbz zzz
aiz zzz czz
zzz izz zbz
zzz zze gzz
    """