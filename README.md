# docs-assembler
Добавляет текст от начального параграфа до конечного (можно указать) из всех файлов Microsoft Word в один

## Параметры

`-h` - помощь

`-p` `--path` - путь, где находятся документы

`-s` `--startph` - параграф, с которого нужно начать копирование (если пустой - копирование начнется с первой строки)

`-e` `--endph` - параграф, до которого нужно завершить копирование (если пустой - копирование завершится в конце документа)


## Использование

python3 docsAssembler.py [-h] [-p *path*] [-s *startphrase*] [-e *endphrase*]

## Requirements

[python-docx](https://pypi.org/project/python-docx/ "python-docx") - `pip install python-docx`
