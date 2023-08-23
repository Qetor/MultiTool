import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

import subprocess

run_in_terminal = 'kgx -e bash -c'

def run_command(command):
    subprocess.Popen(f"export XDG_CONFIG_HOME=/home/elian && {command}", shell=True)

def linux_help(argument):
    run_command(f"{run_in_terminal} 'hx /home/elian/hdd/Programme/linux-tricks.md'")

def poweroff(argument):
    run_command('loginctl poweroff')
    
def music(argument):
    run_command('monophony')
    
def minecraft(argument):
    run_command('prismlauncher')
    
def firefox(argument):
    run_command('firefox')
    
def fluffychat(argument):
    run_command('fluffychat')
    
    
def execute(argument):
    command = entry.get_text()
    run_command(f"{run_in_terminal} '{command}'")

    
def new_button(title, action):
    btn = Gtk.Button(label=title)
    btn.connect('clicked', action)
    return btn


def on_activate(app):
    global win
    win = Gtk.ApplicationWindow(application=app)
    win.set_title("MulitTool")
    win.set_size_request(500, -1)
    
    box = Gtk.Box(spacing=10, orientation=Gtk.Orientation.VERTICAL)
    box.set_margin_end(10)
    box.set_margin_start(10)
    box.set_margin_top(10)
    box.set_margin_bottom(10)
    
    entry_box = Gtk.Box(spacing=10, orientation=Gtk.Orientation.HORIZONTAL)
    
    global entry
    entry = Gtk.Entry()
    entry.set_placeholder_text("Kommando eingeben")
    entry.set_hexpand(True)
    entry_box.append(entry)
    entry_btn = new_button("Ausführen", execute)
    entry_box.append(entry_btn)
    
    for button in (
        new_button("Fluffychat", fluffychat),
        new_button("Firefox", firefox),
        new_button("Minecraft", minecraft),
        new_button("Musik", music),
        new_button("Linux Tricks", linux_help),
        new_button("Ausschalten", poweroff),
        ):
        box.append(button)
        
    box.append(entry_box)
    
    win.set_child(box)
    win.present()

app = Gtk.Application(application_id='org.gtk.Example')
app.connect('activate', on_activate)
app.run(None)
