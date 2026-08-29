const vscode = require("vscode");

let terminal;

const BEFEHL_JE_ENDUNG = {
  ".dpy": "dpy",
  ".lpy": "lpy",
};

function holeTerminal() {
  if (!terminal || terminal.exitStatus !== undefined) {
    terminal = vscode.window.createTerminal("Bilingual-Python");
  }
  return terminal;
}

function activate(context) {
  const befehl = vscode.commands.registerCommand("bilingualpython.ausfuehren", () => {
    const editor = vscode.window.activeTextEditor;
    if (!editor) {
      return;
    }
    editor.document.save().then(() => {
      const pfad = editor.document.fileName;
      const endung = pfad.slice(pfad.lastIndexOf(".")).toLowerCase();
      const laufBefehl = BEFEHL_JE_ENDUNG[endung];
      if (!laufBefehl) {
        vscode.window.showErrorMessage(
          `Bilingual-Python kennt die Dateiendung "${endung}" nicht.`
        );
        return;
      }
      const t = holeTerminal();
      t.show(true);
      t.sendText(`${laufBefehl} "${pfad}"`);
    });
  });
  context.subscriptions.push(befehl);
}

function deactivate() {}

module.exports = { activate, deactivate };
