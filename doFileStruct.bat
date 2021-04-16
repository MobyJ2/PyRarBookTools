@echo off
REM python doFileStruct.py D:\\_todo\\_Temp\\test2.rar

rem Boucle avec un goto pour afficher les variables.
:continue
if "%1"=="" goto fin
echo +++ Start: %1 +++
python doFileStruct.py %1
echo --- End: %1
shift
goto continue
:fin

PAUSE

REM echo Nom du programme : %0
REM echo Ensemble des arguments : %*
REM echo Argument 1 : %1
REM echo Argument 2 : %2
REM echo Argument 3 : %3
REM echo Argument 4 : %4
REM echo Argument 5 : %5
REM echo Argument 6 : %6
REM echo Argument 7 : %7
REM echo Argument 8 : %8
REM echo Argument 9 : %9
