# img_viewer.py
import torch
import PySimpleGUI as sg
import os.path
import torch.nn as nn
import torch.nn.functional as F

from code import utils


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x)


def load_MNIST_classifier(chkpnt):
    network = Net()
    # load checkpoint
    network.load_state_dict(torch.load(chkpnt))
    network.eval()
    return network



def generate_prediction(input_image_fn, MNist_classifier):
    # resize image
    input_image = utils.load_and_scale(input_image_fn)

    image_input = torch.from_numpy(input_image).unsqueeze(0).unsqueeze(0).float()
    output = MNist_classifier(image_input)
    pred = output.data.max(1, keepdim=True)[1]

    return pred.item()



ckpt_filename = "data/pretrained_mnist_weights/model.pth"
digit_classifier = load_MNIST_classifier(ckpt_filename)

# First the window layout in 2 columns

file_list_column = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse()
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
]


# For now will only show the name of the file that was chosen
image_viewer_column = [[
    sg.Text("Choose an image from list on left:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
    [sg.Button('Predict')],
    [sg.Text(size=(40, 1), key="-PREDICTION-")]

]

# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("Image Viewer", layout)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Folder name was filled in, make a list of files in the folder
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif"))
        ]
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-":  # A file was chosen from the listbox

        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)

        except:
            pass

    elif event == "Predict":
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            prediction = generate_prediction(filename, digit_classifier)
            window["-PREDICTION-"].update("The prediction is: " + str(prediction))
        except:
            print("nothing selected!")

window.close()
