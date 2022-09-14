# wows-mod-stat (aka vanga)

## Простой мод для игры World Of Warships 

мод сохраняет статистику боя в разрезе живых кораблей каждую минуту (время задано константой и его можно менять, в этом случае требуется изменение заголовка CSV файла)

мод не выводит стат данные в клиент (разработчики запрещают любое прогнозирование результата в течении боя), все данные служат для послебоевой обработки.
данные сохраняются в CSV файл. Первые пять столбцов содержат общую информацию по бою
- battle_id,            # сгенерированный идентификатор боя в формате ДАТА_ВРЕМЯ(UTC). Последняя буква (L/W) - результат относительно игрока
- my_level,             # уровень лодки игрока (средний уровень посчитать через доступные данные не получилось)
- battle_type,          # тип боя
- battle_duration_sec,  # длительность боя в секундах
- winner_team_id,       # 0 или 1, полезной информации не несет
- t0_m19 - t1_m0        # 20 столбцов (по 10 на команду) с количеством живых лодок. Победившая команда всегда идет первой (чтоб было легче считать разницу. Последний столбец всегда содержит количество живых на момент окончания боя. Если игрок вышел из боя до окончания, данные будут не полными (но последний столбец и результат сохраняется)

### установка
Переписать файлы *battleStatDef.py, Main.py, vanga_result.csv* в каталог модов. (например \World_of_Warships\bin\6223574\res_mods\PnFMods\vanga\). Файл vanga_result.csv будет постоянно пополняться. 
ВНИМАНИЕ! Если используется мод пак, есть риск потери собранных данных, так как мод пак удаляет незнакомые ему моды. (в момент установки / обновления модов)

### благодарности:
* оригинальная идея https://forum.worldofwarships.ru/topic/152030-исследование-предсказуемость-боёв
* прекрасный пример мода, использованный как шаблон и учебник https://github.com/qMBQx8GH/mxmeter


## Simple mod for World Of Warships game
This mod collects the stat info for alive ships during the battle every minute. This time can be changed (remember to adjust the CVS header if needed)

The Mod does not show the stat or stat result in the game as showing any battle result prediction is not allowed. Therefore all the collected data can be used only for post-battle analytics (in Excel/SQL). First five columns contain the general information

- battle_id,            # generated battle id DATE_TIME(UTC). Last letter (L/W) corresponds to the battle result
- my_level,             # the player's ship level (other ships level is not available in the used ModeAPI objects)
- battle_type,          # battletype
- battle_duration_sec,  # battle duration in seconds
- winner_team_id,       # winner_team_id (0 or 1), not really useful for now
- t0_m19 - t1_m0        # 20 columns (10 per each team) containing alive ships numbers. The winning team always goes first to simplify the math. The last column always contains the number of alive ships at the end of the battle. If a user left the battle before the battle ends, remaining columns will not contain the actual data (except the last column and the game results)

### Installation
Put the  *battleStatDef.py, Main.py, vanga_result.csv* files to the Mod folder. (For example \World_of_Warships\bin\6223574\res_mods\PnFMods\vanga\).   Collected data will be stored in *vanga_result.csv*. 
WARNING! If the Mod Station (or any other mod pack is used) there is a risk of losing the collected data, as mod pack controls the mod folder and will delete unknown mods during its update.

### special thanks:
* original idea (in Russian) https://forum.worldofwarships.ru/topic/152030-исследование-предсказуемость-боёв
* great WOWs Mod. Great as a Mod, as a template, as an example. https://github.com/qMBQx8GH/mxmeter
