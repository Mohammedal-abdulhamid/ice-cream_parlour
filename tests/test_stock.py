from src.stock import classify_tub


def test_classify_tub():
  # ARRANGE
    modified_tub = {"flavour": "Vanilla Bean",
    "litres": 4.5,
    "capacity": 5.0,
    "price_per_litre": 3.2}
  #ACT
    result = classify_tub(modified_tub)
    #ASSERT
    assert type(result) == dict
########################################

def test_classify_tub_has_a_status():
  # ARRANGE
    modified_tub = {"flavour": "Vanilla Bean",
    "litres": 4.5,
    "capacity": 5.0,
    "price_per_litre": 3.2}

    #ACT
    classify_tub(modified_tub )
    status_case = "status" in modified_tub
    #ASSERT
    assert   status_case   ==  True



# #############################################

def test_classify_tub_has_a_status_ok():
  # ARRANGE
    modified_tub = {"flavour": "Vanilla Bean",
    "litres": 4.5,
    "capacity": 5.0,
    "price_per_litre": 3.2,
    "status":""
    }


    expected_result  = {"flavour": "Vanilla Bean",
    "litres": 4.5,
    "capacity": 5.0,
    "price_per_litre": 3.2,
    "status":"ok"
    }
   #ACT
    result = classify_tub(modified_tub )

    #ASSERT
    assert  expected_result   ==  result