from pywinauto.application import Application

app = Application().start('notepad.exe')

app.UntitledNotepad.Edit.type_keys('Hello!')

app.UntitledNotepad.menu_select('File->SaveAs')

app.SaveAs.Edit1.set_text('C:\\Users\\korniichuk\\Desktop\\demo.txt')
app.SaveAs.Save.click()

app.demotxtNotepad.menu_select('File->Exit')
