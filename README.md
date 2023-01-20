# Final-Project

The goal of the project is to enabling optimization of anchors’ positions for ground holding walls.
For this purpose, the program simulates forces arising in such situations and calculates mechanical stresses based on finite element methods.
Efficiency of various strategies of anchor placing will be studied. Improvements of such strategies will be searched by the machine learning methods (Monte Carlo simulations, q-learning, gradient descent, branch and bounds,).
Reliability of the results are studied from the comparisons of the obtained results with the published ones for the real ground holding walls.




# Install
pip install django djangorestframework ,
django-admin startproject ground_anchoring_controller ,
cd ground_anchoring_controller ,
django-admin startapp api ,

line code => go to ground_anchoring_controller => settings.py => inside INSTALLED_APPS  add  = 'api.apps.ApiConfig'
line code => go to ground_anchoring_controller => settings.py => inside INSTALLED_APPS  add  = 'rest_framework'

python .\manage.py makemigrations
python .\manage.py migrate
python .\manage.py runserver

# after adding our models update the migrations

python .\manage.py makemigrations
python .\manage.py migrate

# add frontend 

django-admin startapp frontend
⌨ NPM Setup Commands ⌨  => npm i install
npm init -y
npm i webpack webpack-cli --save-dev
npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev
npm i react react-dom --save-dev
npm config set legacy-peer-deps true
npm i
npm install @material-ui/core
npm install @babel/plugin-proposal-class-properties
npm install react-router-dom
npm install @material-ui/icons


npm install react-bootstrap bootstrap
npm install react-bootstrap-validation --save
npm install react-icons

npm install @mui/material @emotion/react @emotion/styled
npm i @mui/material 


