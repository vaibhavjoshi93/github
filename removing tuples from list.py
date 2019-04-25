def removetouples(tuples):
        tuples=filter(None,tuples)
        return tuples

tuples=[(),('ram','15','8'), (),('laxman', 'sita'),('krishna', 'akbar', '45'),('',''),()]
finalans=removetouples(tuples)
finalans1=list(finalans)
print(finalans1)
