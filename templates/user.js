function validateForm() {
    var firstName = document.getElementById("first_name").value;
    var lastName = document.getElementById("last_name").value;
    var mobile = document.getElementById("mobile").value;
    var city = document.getElementById("city").value;
    var firstNameError = document.getElementById("first_name_error");
    var lastNameError = document.getElementById("last_name_error");
    var mobileError = document.getElementById("mobile_error");
    var cityError = document.getElementById("city_error");
    var isValid = true;

    // Validate first name
    if (!/^[a-zA-Z]+$/.test(firstName)) {
        firstNameError.innerHTML = "First name should contain only letters.";
        isValid = false;
    } else {
        firstNameError.innerHTML = "";
    }

    // Validate last name
    if (!/^[a-zA-Z]+$/.test(lastName)) {
        lastNameError.innerHTML = "Last name should contain only letters.";
        isValid = false;
    } else {
        lastNameError.innerHTML = "";
    }

    // Validate mobile number
    if (!/^\d{10}$/.test(mobile)) {
        mobileError.innerHTML = "Mobile number should be exactly 10 digits.";
        isValid = false;
    } else {
        mobileError.innerHTML = "";
    }

    // Validate city name
    if (!/^[a-zA-Z\s]+$/.test(city)) {
        cityError.innerHTML = "City name should contain only letters.";
        isValid = false;
    } else {
        cityError.innerHTML = "";
    }

    return isValid;
}
