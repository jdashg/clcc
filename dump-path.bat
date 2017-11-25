@echo off
echo %INCLUDE% > .cl-path.txt
echo %LIB% >> .cl-path.txt
where cl >> .cl-path.txt
