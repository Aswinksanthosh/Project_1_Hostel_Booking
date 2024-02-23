function isPassedDate() {
    var today = new Date();
    var checkin = new Date(document.getElementById("ckin").value);
    var checkout = new Date(document.getElementById("ckout").value);
    if (checkin <= today) {
        alert("Check-in date must be today or in the future.");
        return false;
    }
    else if (checkin >= checkout) {
        alert("Check-out date must be after check-in date.");
        return false;
    }
    return true;
}
