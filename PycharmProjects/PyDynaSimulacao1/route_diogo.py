import pydyna
from venus.viewer import Venus
from venus.helpers import RelPos
from venus.objects import (
    Vessel,
    GeoPos,
    Rudder,
    Size,
    KeyValue,
    Button,
    Line,
    Panel,
    Polygon,
    Beacon,
    Arrow,
    Checkbox,
    Textbox,
    TextboxType)

from math import sin, cos, pi, radians
from time import sleep

def main():
    # We define a central position. Every `RelPos` from this point on (unless noted) is
    # derived from this.
    central_position = GeoPos(-23.06255, -44.2772)
    RelPos.set_absolute_position(central_position)

    # Create a new Venus instance and change the viewport to look at our central_position.
    venus = Venus(logging=True, port=6150)
    venus.set_viewport(central_position, 15)
    dicionary_circle = {}
    circle = []
    circle_counter = 0
    chk_edit_circle = []



    panel2 = venus.add(
        Panel(
            data_panel=[
                Checkbox("chk_add_circle", "Add circle", False),
                Checkbox("chk_drag_circle", "Drag circle", False),
            ]
        )  ## receber a posição do circulo
    )

    def calc_lat_lon(panel,latitude,longitude):
        pass


    #panel2.data_panel.append(KeyValue("Latitude", ""))

    # Callback for checkboxes
    def on_checkbox_changed(checkbox_uid, checked):

        #list_dictionary_circle = dicionary_circle.values()

        if checkbox_uid == "chk_add_circle":
            if checked:
                panel2.data_panel.append(KeyValue("Latitude", "Min:-90 - Max:90"))
                panel2.data_panel.append(Textbox("lat_pos", -23.06, disabled=False,
                                                     textbox_type=TextboxType.NUMBER, min=-90, max=90))
                panel2.data_panel.append(KeyValue("Longitude", "Min: -180 - Max:180"))
                panel2.data_panel.append(Textbox("lon_pos", -44.27, disabled=False,
                                                 textbox_type=TextboxType.NUMBER, min=-180, max=180))
                panel2.data_panel.append(KeyValue("Raio", "Min: 0 - Max: 1000"))
                panel2.data_panel.append(Textbox("raio_pos", 30, disabled=False,
                                                 textbox_type=TextboxType.NUMBER, min=0, max=1000))
                panel2.data_panel.append(Button("insert", "Insert"))
            else:
                for i in range(2, len(panel2.data_panel)):
                    panel2.data_panel.pop()

        if dicionary_circle[checkbox_uid]:



            # if checkbox_uid == circle[number].data_panel[2]:
            #     circle[number].draggable = checked

            if checkbox_uid == "chk_edit_circle1":
                dicionary_circle.find[checkbox_uid]

                if checked:
                    circle[0].data_panel.append(KeyValue("Latitude", ""))
                    circle[0].data_panel.append(Textbox("lat_pos", '', disabled=False,
                                                         textbox_type=TextboxType.NUMBER, min=0, max=359.9))
                    circle[0].data_panel.append(KeyValue("Longitude", ""))
                    circle[0].data_panel.append(Textbox("lon_pos", '', disabled=False,
                                                     textbox_type=TextboxType.NUMBER, min=0, max=359.9))
                    circle[0].data_panel.append(Button("edit", "Edit"))
                else:
                    for i in range(2, len(panel2.data_panel)):
                        circle[0].data_panel.pop()

        if checkbox_uid == "chk_drag_circle":
            for number_circles in range(len(dicionary_circle)):
                circle[number_circles].draggable = checked


    def on_button_clicked(button_uid):
        nonlocal circle_counter

        chk_edit_circle_by_button = "chk_del_button{}".format(str(circle_counter))
        chk_edit_circle_by_checkbox = "chk_edit_circle_by_checkbox{}".format(str(circle_counter))
        chk_drag_circle_by_checkbox = "chk_drag_circle_by_checkbox{}".format(str(circle_counter))




        if button_uid == "chk_edit_circle1":
            pass

        if button_uid == "insert":
            latitude_new_point = 0.0
            longitude_new_point = 0.0
            radius_new_point = 0.0

            # if not panel2.data_panel[3].value: # pegar a latitude
            #     latitude_new_point = central_position.latitude
            # else:
            #     latitude_new_point = float(panel2.data_panel[3].value)
            #
            # if not panel2.data_panel[5].value: # pegar a longitude
            #     longitude_new_point = central_position.longitude
            # else:
            #     longitude_new_point = float(panel2.data_panel[5].value)
            #
            # if not panel2.data_panel[7].value: #pegar o raio
            #     radius_new_point = 5.0
            # else[
            #     radius_new_point = float(panel2.data_panel[7].value)

            calc_latitude_Relative =  - central_position.latitude + float(panel2.data_panel[3].value)
            calc_longitude_Relative = - central_position.longitude + float(panel2.data_panel[5].value)

            radius_new_point = float(panel2.data_panel[7].value)

            circle.append(
                venus.add(
                    Polygon(
                        # These points define a 360-sided polygon
                        points=[
                            RelPos(sin(radians(n)) * radius_new_point - calc_latitude_Relative, cos(radians(n)) * radius_new_point - calc_longitude_Relative).to_geo()
                            #RelPos(-500 * sin(radians(n))-700,-500 * cos(radians(n))-600).to_geo()
                            for n in range(0, 360, int(2 * pi))
                        ],

                        # Visual options for the polygon
                        visual_options={"color": "red", "fillOpacity": 0.1, "weight": 3},

                        # Some test properties on the data panel
                        data_panel=[
                            Checkbox(chk_edit_circle_by_checkbox,"Edit circle", False),
                            Button(chk_edit_circle_by_button, "Delete circle"),
                            Checkbox(chk_drag_circle_by_checkbox, "Drag circle", False),
                        ],

                        # This polygoragged by the user
                        draggable=False
                        ,
                        )
                    )
                )

            dicionary_circle['circle{}'.format(circle_counter)] = (chk_drag_circle_by_checkbox , chk_edit_circle_by_button,chk_edit_circle_by_checkbox)


            chk_edit_circle.append(chk_edit_circle_by_button)

            circle_counter += 1

        #btn_delete_circle =

        chk_edit_circle_button = chk_edit_circle[:]

        if button_uid in chk_edit_circle:
            for i in range(len(chk_edit_circle)):
                if button_uid == chk_edit_circle[i]:
                    venus.remove(circle[i])
                    del circle[i]

                    circle_counter -= 1

        # if button_uid[0:14] == "chk_del_button":
        #     i = int(button_uid[14])
        #     venus.remove(circle[int(button_uid[14])])
        #     del(circle[int(button_uid[14])])
        #
        #     circle_counter -= 1




    venus.on_checkbox_changed = on_checkbox_changed
    venus.on_button_clicked = on_button_clicked



if __name__ == "__main__":
    main()