const vscode = require("vscode");

let terminal;

function holeTerminal() {
  if (!terminal || terminal.exitStatus !== undefined) {
    terminal = vscode.window.createTerminal("Deutsch-Python");
  }
  return terminal;
}

function activate(context) {
  const befehl = vscode.commands.registerCommand("deutschpython.ausfuehren", () => {
    const editor = vscode.window.activeTextEditor;
    if (!editor) {
      return;
    }
    editor.document.save().then(() => {
      const pfad = editor.document.fileName;
      const t = holeTerminal();
      t.show(true);
      t.sendText(`dpy "${pfad}"`);
    });
  });
  context.subscriptions.push(befehl);
}

function deactivate() {}

module.exports = { activate, deactivate };
