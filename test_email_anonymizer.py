
TEST_DATA = [
    ("Lorem ipsum", "Lorem ipsum"),
    ("Lorem ipsum a@a.com dolor sit amet", "Lorem ipsum ...@a.com dolor sit amet"),
    ("Lorem ipsum --@--.--", "Lorem ipsum --@--.--"),
    ("Lorem some@data ipsum", "Lorem some@data ipsum"),
    ("Lorem B@bb12.com ipsum", "Lorem ...@bb12.com ipsum"),
    ("Lorem abc-abc@abc.edu.co.uk am", "Lorem ...@abc.edu.co.uk am"),
    ("Lorem cBa-abC@abc.edu.co.uk. dolor", "Lorem ...@abc.edu.co.uk. dolor"),
    ("Lorem dsad BB12@BB-12.COM. dolor", "Lorem dsad ...@BB-12.COM. dolor"),
    ("Lorem XXd -abc_ABC@abc.edu. dolor", "Lorem XXd -...@abc.edu. dolor"),
]


