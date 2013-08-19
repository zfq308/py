VERSION 5.00
Begin VB.Form Form1 
   Caption         =   "Form1"
   ClientHeight    =   5415
   ClientLeft      =   120
   ClientTop       =   450
   ClientWidth     =   11295
   LinkTopic       =   "Form1"
   ScaleHeight     =   5415
   ScaleWidth      =   11295
   StartUpPosition =   3  '´°¿ÚÈ±Ê¡
   Begin VB.CommandButton upload 
      Caption         =   "Command1"
      Height          =   735
      Left            =   2040
      TabIndex        =   7
      Top             =   4440
      Width           =   1215
   End
   Begin VB.TextBox Text2 
      Height          =   375
      Left            =   360
      TabIndex        =   4
      Text            =   "Text2"
      Top             =   2400
      Width           =   4695
   End
   Begin VB.TextBox Text1 
      Height          =   375
      Left            =   360
      TabIndex        =   3
      Text            =   "Text1"
      Top             =   960
      Width           =   4695
   End
   Begin VB.CommandButton confirm 
      Caption         =   "Command2"
      Height          =   735
      Index           =   1
      Left            =   360
      TabIndex        =   2
      Top             =   4440
      Width           =   1215
   End
   Begin VB.CommandButton quit 
      Cancel          =   -1  'True
      Caption         =   "Command1"
      Height          =   735
      Index           =   0
      Left            =   3720
      TabIndex        =   1
      Top             =   4440
      Width           =   1215
   End
   Begin VB.ListBox List1 
      Appearance      =   0  'Flat
      Height          =   5070
      Left            =   5520
      TabIndex        =   0
      Top             =   240
      Width           =   5535
   End
   Begin VB.Label Label2 
      Caption         =   "Label2"
      Height          =   375
      Left            =   360
      TabIndex        =   6
      Top             =   1800
      Width           =   2175
   End
   Begin VB.Label Label1 
      Caption         =   "Label1"
      Height          =   375
      Left            =   360
      TabIndex        =   5
      Top             =   360
      Width           =   2055
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub Dir1_Change()

End Sub
