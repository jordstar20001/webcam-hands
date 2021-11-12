import tensorflow as tf
import keras
import numpy as np
from timeit import default_timer as timer
from webcam_hands_utils import trained_gestures
# Create test np arrays
# FIST
first_test = np.array([list(map(float, "1,0.35734763741493225,0.5673075318336487,3.2510525382889455,0.32293403148651123,0.550406813621521,0.004081607796251774,0.28909212350845337,0.5153418183326721,0.008981938473880291,0.2698686420917511,0.4804365932941437,0.017793137580156326,0.27708667516708374,0.4489140808582306,0.023561714217066765,0.3082064986228943,0.4548557996749878,0.012902614660561085,0.28509536385536194,0.4270869791507721,0.008076736703515053,0.287916898727417,0.4614318311214447,0.009960366412997246,0.30099961161613464,0.47981807589530945,0.011229640804231167,0.325187623500824,0.4474998414516449,0.004475986585021019,0.2974301278591156,0.42588087916374207,0.011103251948952675,0.3035503029823303,0.4711451530456543,0.015939753502607346,0.31883934140205383,0.48122698068618774,0.013617245480418205,0.34434157609939575,0.4436282813549042,0.006014575250446796,0.3164216876029968,0.4285164475440979,0.021169615909457207,0.32174941897392273,0.47202980518341064,0.020800428465008736,0.3384936451911926,0.48329731822013855,0.01562361977994442,0.36749404668807983,0.4428384006023407,0.017864858731627464,0.3382410705089569,0.4291074573993683,0.02420242503285408,0.3374227285385132,0.46014711260795593,0.021722400560975075,0.35025885701179504,0.47236016392707825,0.01767280511558056".split(',')))])

# PEACE
second_test = np.array([list(map(float, "1,0.37501293420791626,0.7398377656936646,2.8857554124073204,0.32742762565612793,0.6970138549804688,0.005283301696181297,0.29633331298828125,0.6275957226753235,0.01625286415219307,0.291462242603302,0.5717334151268005,0.034950777888298035,0.32326939702033997,0.5475917458534241,0.05198238790035248,0.32710790634155273,0.5453919172286987,0.012275087647140026,0.2964380383491516,0.47487738728523254,0.005975713487714529,0.2798870801925659,0.433224618434906,0.01828850246965885,0.26772618293762207,0.39827150106430054,0.028264127671718597,0.3590087294578552,0.5406284332275391,0.008355298079550266,0.3575289249420166,0.44505882263183594,0.03146040067076683,0.3499215245246887,0.3897166848182678,0.04845666512846947,0.34486275911331177,0.3461063802242279,0.06017368659377098,0.3865502178668976,0.556268036365509,0.03302157670259476,0.3575475513935089,0.5038141012191772,0.06192290037870407,0.3318016529083252,0.5565447807312012,0.06206417456269264,0.3248130679130554,0.5975586771965027,0.055922504514455795,0.4069337844848633,0.5852497220039368,0.061130449175834656,0.3765113055706024,0.545907199382782,0.08423366397619247,0.3516680598258972,0.5821716785430908,0.08258481323719025,0.3439885079860687,0.6174893975257874,0.0766805037856102".split(',')))])

# Load the model using keras
model = keras.models.load_model("gesture_classifier_model")

# Check if the model returns the correct

t1 = timer()
v = np.argmax(model.predict(first_test)[0])
t2 = timer()
print(trained_gestures[v])
print(f"Prediction took: {t2-t1} seconds!\nThat means, without considering other factors, you could run at {1/(t2-t1)} fps..!")

t1 = timer()
v = np.argmax(model.predict(first_test)[0])
t2 = timer()
print(trained_gestures[v])
print(f"Prediction took: {t2-t1} seconds!\nThat means, without considering other factors, you could run at {1/(t2-t1)} fps..!")