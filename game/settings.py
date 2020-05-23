from pathlib import Path

GAME_TITLE = 'Unige'
FPS = 60
SCREEN_WIDTH = 840
SCREEN_HEIGHT = 650

root_dir = Path.cwd()
src_dir = root_dir / 'game/'
res_dir = root_dir / 'res/'

ui_res = res_dir / 'ui/'
fonts_res = res_dir / 'fonts/'
player_res = res_dir / 'player/'
slime_res = res_dir / 'enemies' / 'slime'