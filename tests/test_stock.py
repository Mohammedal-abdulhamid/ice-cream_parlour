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
    tub = {"flavour": "Vanilla Bean",
    "litres": 4.5,
    "capacity": 5.0,
    "price_per_litre": 3.2}

    #ACT
    status_case = "status" in  classify_tub(tub)
    #ASSERT
    assert   status_case   ==  True



# #############################################

def test_classify_tub_has_a_status_ok():
  # ARRANGE
    modified_tub = {"flavour": "Vanilla Bean",
    "litres": 4.5,
    "capacity": 5.0,
    "price_per_litre": 3.2,
    
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

def test_classify_tub_has_a_status_low():
  # ARRANGE
    modified_tub = {"flavour": "Vanilla Bean",
    "litres": 3.0,
    "capacity": 5.0,
    "price_per_litre": 3.2,
    
    }


    expected_result  = {"flavour": "Vanilla Bean",
    "litres": 3.0,
    "capacity": 5.0,
    "price_per_litre": 3.2,
    "status":"low"
    }
   #ACT
    result = classify_tub(modified_tub )

    #ASSERT
    assert  expected_result   ==  result

##############################################
def test_classify_tub_has_a_status_reorder():
  # ARRANGE
    modified_tub = {"flavour": "Vanilla Bean",
    "litres": 1.0,
    "capacity": 5.0,
    "price_per_litre": 3.2,
    
    }


    expected_result  = {"flavour": "Vanilla Bean",
    "litres": 1.0,
    "capacity": 5.0,
    "price_per_litre": 3.2,
    "status":"reorder"
    }
   #ACT
    result = classify_tub(modified_tub )

    #ASSERT
    assert  expected_result   ==  result