import functions.cals as fc

def test_negatives():
    assert adivb(-10,-5) == 2, "two negatives return a postive"
    #assert adivb(-9,3) <0, "one +ve, 1 -ve reurns -ve"
    #assert adivb(35,7)>0, "2 positives should be positive"
    #assert isinstance(adivb(5,10), float), "minor by larger should be float"
    #assert type(adivb(5,10))== type(1.0)
    #assert adivb(5,2)==2.5, "5 divided by 2 should be 2.5"
    #assert adivb(10,3)==pytest.approx(3.33,0.01), "10 div by 3 is 3.33333"