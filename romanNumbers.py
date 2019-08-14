def roman():
    romanNumerals = ["I","II","III","IV","V","VI","VII","IIX","IX","X","XI","XII","XIII","XIV","XV","XVI","XVII","XVIII","XIX","XX","XXI","XXII","XXIII","XXIV","XXV","XXVI","XXVIII","XXIX","XXX","XXXI","XXXII","XXXIII","XXXIV","XXXV","XXXVI","XXXVII","XXXVIII","XXXIX","XL","XLI","XLII","XLIII","XLIV","XLV","XLVI","XLVII","XLVIII","XLIX","L"]
    num = int(input("Enter an Intiger number between 0-50: "))
    if (num > 0 and num <= 50):
        print(romanNumerals[num-1])
    else:
        print("Error")