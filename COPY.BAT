SET CHANNEL=Android_360

SET SRC=D:\repo\MLDJClient\Version\Main\Project\Client\AndroidPlugins\
SET TARGET=D:\repo\MLDJClient\Version\TY\Project\Client\AndroidPlugins\

IF EXIST %TARGET%%CHANNEL% RD /S/Q %TARGET%%CHANNEL%

XCOPY /Y/E/R %SRC%%CHANNEL% %TARGET%%CHANNEL%\

PAUSE