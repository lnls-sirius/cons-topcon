#!/usr/bin/python3
from string import Template

SELECT_SYSTEM = ("""
selectSystem{
    MaxInput = 5;
    out "\\xA5\\x06\\x11\\xD0\\x50\\x00", "\\x40\\x00", "%2<sum>", "%#/(?sm)(..)(......)(.)/\\1\\3\\2/";
    in  "%#/(?sm)(..)(.)(..)/\\1\\3\\2/", "\\xA5\\x02\\x11\\x00", "%2<sum>";
}
""")

SELECT_MASTER = ("""
selectMaster{
    MaxInput = 5;
    out "\\xA5\\x06\\x11\\xD0\\x50\\x00", "\\x00\\x00", "%2<sum>", "%#/(?sm)(..)(......)(.)/\\1\\3\\2/";
    in  "%#/(?sm)(..)(.)(..)/\\1\\3\\2/", "\\xA5\\x02\\x11\\x00", "%2<sum>";
}
""")

UINT16_W_1 = Template("""
$proto{
    MaxInput = 5;
    out "\\xA5\\x06\\x11$address", "\\x01\\x00", "%2<sum>", "%#/(?sm)(..)(......)(.)/\\1\\3\\2/";
    in  "%#/(?sm)(..)(.)(..)/\\1\\3\\2/", "\\xA5\\x02\\x11\\x00", "%2<sum>";
}
""")

UINT16_W = Template("""
$proto{
    MaxInput = 5;
    out "\\xA5\\x06\\x11$address", "%#0.2r", "%2<sum>", "%#/(?sm)(..)(......)(.)/\\1\\3\\2/";
    in  "%#/(?sm)(..)(.)(..)/\\1\\3\\2/", "\\xA5\\x02\\x11\\x00", "%2<sum>";
    @mismatch{ in "\?", "\?", "%(\\$$1_error)#1r", "\?", "\?"; }
}
""")

UINT16_R = Template("""
$proto{
    MaxInput = 7;
    out "\\xA5\\x04\\x10$address", "%2<sum>", "%#/(?sm)(..)(....)(.)/\\1\\3\\2/";
    in  "%#/(?sm)(..)(.)(....)/\\1\\3\\2/", "\\xA5\\x04\\x10\\x00", "%#02r", "%2<sum>";
    @mismatch{ in "\?", "\?", "\?", "\?", "%(\\$$1_error)#1r", "\?", "\?"; }
}
""")

SINT16_R = Template("""
$proto{
    MaxInput = 7;
    out "\\xA5\\x04\\x10$address", "%2<sum>", "%#/(?sm)(..)(....)(.)/\\1\\3\\2/";
    in  "%#/(?sm)(..)(.)(....)/\\1\\3\\2/", "\\xA5\\x04\\x10\\x00", "%#2r", "%2<sum>";
    @mismatch{ in "\?", "\?", "\?", "\?", "%(\\$$1_error)#1r", "\?", "\?"; }
}
""")

SINT16_W = Template("""
$proto{
    MaxInput = 5;
    out "\\xA5\\x06\\x11$address", "%#.2r", "%2<sum>", "%#/(?sm)(..)(......)(.)/\\1\\3\\2/";
    in  "%#/(?sm)(..)(.)(..)/\\1\\3\\2/", "\\xA5\\x02\\x11\\x00", "%2<sum>";
    @mismatch{ in "\?", "\?", "%(\\$$1_error)#1r", "\?", "\?"; }
}
""")

SELECT_R_INDEX = Template("""
$proto_{
    ${SELECT};
    ${proto};
    @mismatch{ in "\?", "\?", "\?", "\?", "%(\\$$1_error)#1r", "\?", "\?"; }
}""")

SELECT_W_INDEX = Template("""
$proto_{
    ${SELECT};
    ${proto};
    @mismatch{ in "\?", "\?", "%(\\$$1_error)#1r", "\?", "\?"; }
}
""")

