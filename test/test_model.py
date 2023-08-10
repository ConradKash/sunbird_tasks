from app.model import predicted_language

def test_acholi():
    assert predicted_language("Kumbedi abedo Anaka i Amuru aa ki California i Amerika ento.") == 'Acholi'
    
    
def test_english():
    assert predicted_language("I am going to the ") == 'English'
    
def test_lugbara():
    assert predicted_language("Ale mi ra!") == 'lugbara'
    
def test_luganda():
    assert predicted_language("Ebigambo by'amagezi") == 'luganda'
    
def test_runyankole():
    assert predicted_language("Ekiro twaburayo kimwe kyonka tukajaguza embaga y'omwaka") == 'Runyankole'