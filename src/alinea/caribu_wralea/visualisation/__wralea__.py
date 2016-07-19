
# This file has been generated at Fri Aug 03 14:33:53 2012

from openalea.core import *


__name__ = 'alinea.caribu.visualisation'

__editable__ = True
__description__ = ' Visualisation tools for the Caribu package '
__license__ = ''
__url__ = ''
__alias__ = ['Caribu.Visualisation']
__version__ = '0.0.3'
__authors__ = 'C. Pradal'
__institutes__ = 'CIRAD'
__icon__ = ''


__all__ = ['_150127472', 'gammaTrans_gammaTrans', 'saveImage_saveImage', 'colorScale_colorScale', 'ViewMapOnCan', 'py_canview_plot_can', 'py_canview_read_can']



_150127472 = CompositeNodeFactory(name='Plot CaribuScene',
                             description='display a 3D plot of a Caribuscene',
                             category='visualisation',
                             doc='',
                             inputs=[{  'desc': '', 'interface': None, 'name': 'CaribuScene', 'value': None}],
                             outputs=[{  'desc': '', 'interface': None, 'name': 'PlantGL Scene'}],
                             elt_factory={  5: ('vplants.plantgl.visualization', 'plot3D'),
   6: ('alinea.caribu', 'generate scene')},
                             elt_connections={  5092428: (5, 0, '__out__', 0),
   5092440: ('__in__', 0, 6, 0),
   5092452: (6, 0, 5, 0)},
                             elt_data={  5: {  'block': False,
         'caption': 'plot3D',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x07FAB1D0> : "plot3D"',
         'hide': True,
         'id': 5,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': 143.89304436535957,
         'posy': -393.17852282601,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   6: {  'block': False,
         'caption': 'generate scene',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0x07C89B30> : "generate scene"',
         'hide': True,
         'id': 6,
         'lazy': True,
         'port_hide_changed': set(),
         'posx': 120.06352154531945,
         'posy': -445.85364041604765,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   '__in__': {  'block': False,
                'caption': 'In',
                'delay': 0,
                'hide': True,
                'id': 0,
                'lazy': True,
                'minimal': False,
                'port_hide_changed': set(),
                'posx': 150.0,
                'posy': -550.25,
                'priority': 0,
                'use_user_color': False,
                'user_application': None,
                'user_color': None},
   '__out__': {  'block': False,
                 'caption': 'Out',
                 'delay': 0,
                 'hide': True,
                 'id': 1,
                 'lazy': True,
                 'minimal': False,
                 'port_hide_changed': set(),
                 'posx': 153.30052005943537,
                 'posy': -342.69613670133737,
                 'priority': 0,
                 'use_user_color': False,
                 'user_application': None,
                 'user_color': None}},
                             elt_value={  5: [], 6: [(1, 'None')], '__in__': [], '__out__': [(0, "''")]},
                             elt_ad_hoc={  5: {'useUserColor': False, 'position': [143.89304436535957, -393.17852282601], 'userColor': None},
   6: {'useUserColor': False, 'position': [120.06352154531945, -445.85364041604765], 'userColor': None},
   '__in__': {'position': [150.0, -550.25], 'userColor': None, 'useUserColor': False},
   '__out__': {'position': [153.30052005943537, -342.69613670133737], 'userColor': None, 'useUserColor': False}},
                             lazy=True,
                             eval_algo='LambdaEvaluation',
                             )




gammaTrans_gammaTrans = Factory(name='gammaTrans',
                authors='C. Pradal (wralea authors)',
                description='return value normalised and raised at exponent gamma',
                category='Unclassified',
                nodemodule='alinea.caribu.visualisation.gammaTrans',
                nodeclass='gammaTrans',
                inputs=[{'interface': None, 'name': 'values', 'value': None, 'desc': ''}, {'interface': IFloat, 'name': 'gamma', 'value': 1, 'desc': ''}, {'interface': IFloat, 'name': 'minval', 'value': None, 'desc': ''}, {'interface': IFloat, 'name': 'maxval', 'value': None, 'desc': ''}],
                outputs=[{'interface': ISequence, 'name': 'res', 'desc': ''}],
                widgetmodule=None,
                widgetclass=None,
               )




saveImage_saveImage = Factory(name='saveImage',
                authors='C. Pradal, JC Soulie, D. Luquet (wralea authors)',
                description='',
                category='Unclassified',
                nodemodule='alinea.caribu.visualisation.saveImage',
                nodeclass='saveImage',
                inputs=[{'interface': IFileStr, 'name': 'image_name', 'value': None, 'desc': ''}, {'interface': IInterface, 'name': 'scene', 'value': None, 'desc': ''}],
                outputs=[{'interface': IInterface, 'name': 'scene', 'desc': ''}],
                widgetmodule=None,
                widgetclass=None,
               )




colorScale_colorScale = Factory(name='colorScale',
                authors='C. Pradal (wralea authors)',
                description='Produce an plot of the colorscale used by ViewMapOnCan when gamma == 1',
                category='visualisation',
                nodemodule='alinea.caribu.visualisation.colorScale',
                nodeclass='colorScale',
                inputs=[{'interface': None, 'name': 'minval', 'value': None, 'desc': 'min value of the data'}, {'interface': IFloat, 'name': 'maxval', 'value': None, 'desc': 'max value of the data'}, {'interface': IStr, 'name': 'label', 'value': None, 'desc': 'axis label'}],
                outputs=[{'interface': None, 'name': 'fig', 'desc': ''}],
                widgetmodule=None,
                widgetclass=None,
               )




ViewMapOnCan =Factory(name='ViewMapOnCan',
                      description='Jet ColoMapr projection of values on 3D scene ',
                      category='visualisation',
                      nodemodule='alinea.caribu.CaribuScene_nodes',
                      nodeclass='ViewMapOnCan',
                      inputs=[
   {  'desc': '', 'interface': None, 'name': 'CaribuScene', 'value': None},
   {  'desc': '', 'interface': None, 'name': 'Values', 'value': None},
   {  'desc': '', 'interface': IFloat, 'name': 'gamma', 'value': 0.2},
   {  'desc': '', 'interface': IFloat, 'name': 'minval', 'value': None},
   {  'desc': '', 'interface': IFloat, 'name': 'maxval', 'value': None}],
                     outputs=[
                                 {  'desc': '', 'interface': None, 'name': 'CaribuScene'},
                                {  'desc': '', 'interface': None, 'name': 'PlantGL Scene'},
                                {  'desc': '', 'interface': None, 'name': 'values'}],
                             widgetmodule=None,
                widgetclass=None,
               )




py_canview_plot_can = Factory(name='Plot Can File',
                authors='C. Pradal (wralea authors)',
                description='Simple Plot of a can file',
                category='Visualisation.Caribu',
                nodemodule='alinea.caribu.visualisation.py_canview',
                nodeclass='plot_can',
                inputs=[{'interface': IFileStr(filter="*.can", save=False), 'name': 'can file'}, {'interface': ISequence, 'name': 'colors', 'value': None}],
                outputs=[{'name': 'Canestra file'}, {'name': 'Scene'}],
                widgetmodule=None,
                widgetclass=None,
               )




py_canview_read_can = Factory(name='Import Can File',
                authors='C. Pradal (wralea authors)',
                description='ld a detailled description of a can file',
                category='IO, Visualisation.Caribu',
                nodemodule='alinea.caribu.visualisation.py_canview',
                nodeclass='read_can',
                inputs=[{'interface': IFileStr(filter="*.can", save=False), 'name': 'can file'}],
                outputs=[{'name': 'Canestra Scene'}],
                widgetmodule=None,
                widgetclass=None,
               )




