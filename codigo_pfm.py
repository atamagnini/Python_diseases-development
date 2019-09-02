# !/usr/bin/python
# -*- coding: utf-8-*-

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

idh = pd.read_csv(r'fileroot\idh_csv.csv',
                  sep = ';', header = [0])

salud = pd.read_csv(r'fileroot\salud_csv.csv',
                    sep = ';', header = [0])

merged_df = pd.merge(left=idh, right=salud, how='left', left_on='Paises',
                     right_on='Paises')

df = merged_df.sort_values(by='IDH', ascending=True)

#Exportación de tabla de salud e IDH:
df.to_csv(r'fileroot\tabla_salud_idh')

#Gráfico: distribución de países por categoría de IDH (alto, medio, bajo)
plot = df['Categoria'].value_counts().plot(kind='pie', autopct='%.0f%%', 
                                           figsize=(6,6), shadow=True,
                                           explode=(0, 0, 0.15),
                                           startangle=90)
plt.ylabel('')
plt.show()

#Gráfico: clasificación de enfermedades terminales por categoría de IDH
h = df.groupby(['Categoria'])['Neoplasmas_malignos'].sum()
i = df.groupby(['Categoria'])['Enfermedad_Alzheimer_y_otras_demencias'].sum()
j = df.groupby(['Categoria'])['Miocardiopatia_miocarditis_endocarditis'].sum()
k = df.groupby(['Categoria'])['Enfermedad_Pulmonar_Obstructiva_Cronica'].sum()
l = df.groupby(['Categoria'])['Cirrosis_del_higado'].sum()
frames = [h,i,j,k,l]
df2 = pd.concat(frames, axis=1)
df2.plot(kind="bar",figsize=(8,8), stacked=False)
plt.show()

#tabla: totales de enfermedades terminales
n = df2.sum(axis=0)
n = pd.DataFrame(n, columns=['Total'])
print(n)
n.to_csv(r'fileroot\total_enfermedades')

#Gráfico: distribución de enfermedades terminales
plot_2 = n['Total'].plot(kind='pie',autopct='%.0f%%', figsize=(6,6), shadow=True,
           explode=(0, 0, 0, 0, 0.15), startangle=90, labels=['','','','',''])
plt.legend(loc="upper left", bbox_to_anchor=(1,1), labels=n.index)
plt.ylabel('')
plt.show()

Alto = df[df.Categoria == 'Alto']
Medio = df[df.Categoria == 'Medio']
Bajo = df[df.Categoria == 'Bajo']

#Gráfico: dispersión de enfermedades terminales por IDH Bajo
plt.figure(figsize=(8,8))
plt.scatter(Bajo['IDH'], Bajo['Neoplasmas_malignos'], 
             c='blue', s=30, label='Neoplasmas malignos')
plt.scatter(Bajo['IDH'], Bajo['Enfermedad_Alzheimer_y_otras_demencias'], 
             c='orange', s=30, label='Enfermedad Alzheimer y otras demencias')
plt.scatter(Bajo['IDH'], Bajo['Miocardiopatia_miocarditis_endocarditis'],
             c='green', s=30, label='Miocardiopatia miocarditis endocarditis')
plt.scatter(Bajo['IDH'], Bajo['Enfermedad_Pulmonar_Obstructiva_Cronica'], 
             c='red', s=30, label='Enfermedad Pulmonar Obstructiva Cronica')
plt.scatter(Bajo['IDH'], Bajo['Cirrosis_del_higado'], 
             c='purple', s=30, label='Cirrosis del higado')
plt.xlabel('IDH Bajo: (< 0,50)')
plt.ylabel('Cantidad de enfermedades')
plt.legend(loc='best')
plt.show()

#Gráfico: dispersión de enfermedades terminales por IDH Medio
plt.figure(figsize=(15,8))
plt.scatter(Medio['IDH'], Medio['Neoplasmas_malignos'], 
             c='blue', s=10, label='Neoplasmas malignos')
plt.scatter(Medio['IDH'], Medio['Enfermedad_Alzheimer_y_otras_demencias'], 
             c='orange', s=10, label='Enfermedad Alzheimer y otras demencias')
plt.scatter(Medio['IDH'], Medio['Miocardiopatia_miocarditis_endocarditis'],
             c='green', s=10, label='Miocardiopatia miocarditis endocarditis')
plt.scatter(Medio['IDH'], Medio['Enfermedad_Pulmonar_Obstructiva_Cronica'], 
             c='red', s=10, label='Enfermedad Pulmonar Obstructiva Cronica')
plt.scatter(Medio['IDH'], Medio['Cirrosis_del_higado'], 
             c='purple', s=10, label='Cirrosis del higado')
plt.xlabel('IDH Medio: (0,50 a 0,79)')
plt.ylabel('Cantidad de enfermedades')
plt.legend(loc='best')
plt.show()

#Gráfico: dispersión de enfermedades terminales por IDH Alto
plt.figure(figsize=(8,8))
plt.scatter(Alto['IDH'], Alto['Neoplasmas_malignos'], 
             c='blue', s=20, label='Neoplasmas malignos')
plt.scatter(Alto['IDH'], Alto['Enfermedad_Alzheimer_y_otras_demencias'], 
             c='orange', s=20, label='Enfermedad Alzheimer y otras demencias')
plt.scatter(Alto['IDH'], Alto['Miocardiopatia_miocarditis_endocarditis'],
             c='green', s=20, label='Miocardiopatia miocarditis endocarditis')
plt.scatter(Alto['IDH'], Alto['Enfermedad_Pulmonar_Obstructiva_Cronica'], 
             c='red', s=20, label='Enfermedad Pulmonar Obstructiva Cronica')
plt.scatter(Alto['IDH'], Alto['Cirrosis_del_higado'], 
             c='purple', s=20, label='Cirrosis del higado')
plt.xlabel('IDH Alto: (> 0,80)')
plt.ylabel('Cantidad de enfermedades')
plt.legend(loc='best')
plt.show()

#Gráfico: Neoplasmas malignos por categoría de IDH
sns.set(style="ticks", color_codes=True)
g = sns.FacetGrid(df, col="Categoria")
g = g.map(plt.scatter, "Neoplasmas_malignos", "Total")
g.axes[0,0].set_xlabel('Neoplasmas malignos')
g.axes[0,1].set_xlabel('Neoplasmas malignos')
g.axes[0,2].set_xlabel('Neoplasmas malignos')
g.axes[0,0].set_ylabel('Cantidad de enfermedades')

#Gráfico: Enfermedad de Alzheimer y otras demencias por categoría de IDH
sns.set(style="ticks", color_codes=True)
g = sns.FacetGrid(df, col="Categoria")
g = g.map(plt.scatter, "Enfermedad_Alzheimer_y_otras_demencias", "Total")
g.axes[0,0].set_xlabel('Enf. Alzheimer y otras')
g.axes[0,1].set_xlabel('Enf. Alzheimer y otras')
g.axes[0,2].set_xlabel('Enf. Alzheimer y otras')
g.axes[0,0].set_ylabel('Cantidad de enfermedades')

#Gráfico: Miocardiopatia, miocarditis y endocarditis por categoría de IDH
sns.set(style="ticks", color_codes=True)
g = sns.FacetGrid(df, col="Categoria")
g = g.map(plt.scatter, "Miocardiopatia_miocarditis_endocarditis", "Total")
g.axes[0,0].set_xlabel('Miocardiopatia, miocarditis')
g.axes[0,1].set_xlabel('Miocardiopatia, miocarditis')
g.axes[0,2].set_xlabel('Miocardiopatia, miocarditis')
g.axes[0,0].set_ylabel('Cantidad de enfermedades')

#Gráfico: Enfermedad Pulmonar Obstructiva Cronica por categoría de IDH
sns.set(style="ticks", color_codes=True)
g = sns.FacetGrid(df, col="Categoria")
g = g.map(plt.scatter, "Enfermedad_Pulmonar_Obstructiva_Cronica", "Total")
g.axes[0,0].set_xlabel('EPOC')
g.axes[0,1].set_xlabel('EPOC')
g.axes[0,2].set_xlabel('EPOC')
g.axes[0,0].set_ylabel('Cantidad de enfermedades')

#Gráfico: Cirrosis del hígado por categoría de IDH
sns.set(style="ticks", color_codes=True)
g = sns.FacetGrid(df, col="Categoria")
g = g.map(plt.scatter, "Cirrosis_del_higado", "Total")
g.axes[0,0].set_xlabel('Cirrosis del higado')
g.axes[0,1].set_xlabel('Cirrosis del higado')
g.axes[0,2].set_xlabel('Cirrosis del higado')
g.axes[0,0].set_ylabel('Cantidad de enfermedades')
plt.show()

#Gráfico: Distribución del total de enfermedades terminales por categoría de IDH y por enfermedad
m = sns.pairplot(df, hue="Categoria", diag_kind="kde",
                 markers=["o", "s", "D"], height=2, size=3.5,
                       x_vars=["Neoplasmas_malignos",
                               "Enfermedad_Alzheimer_y_otras_demencias",
                               "Miocardiopatia_miocarditis_endocarditis",
                               "Enfermedad_Pulmonar_Obstructiva_Cronica",
                               "Cirrosis_del_higado"],
                               y_vars=["Total"])
plt.show()

salud_porc = pd.read_csv(r'fileroot\salud_csv_porcentajes.csv',
                    sep = ';', header = [0])

merged_df3 = pd.merge(left=idh, right=salud_porc, how='left', left_on='Paises',
                     right_on='Paises')

df3 = merged_df3.sort_values(by='IDH', ascending=True)

#Gráfico: promedios de mortalidad por categoría de IDH
u = df3.groupby(['Categoria'])['Neoplasmas_malignos'].mean()
v = df3.groupby(['Categoria'])['Enfermedad_Alzheimer_y_otras_demencias'].mean()
w = df3.groupby(['Categoria'])['Miocardiopatia_miocarditis_endocarditis'].mean()
x = df3.groupby(['Categoria'])['Enfermedad_Pulmonar_Obstructiva_Cronica'].mean()
y = df3.groupby(['Categoria'])['Cirrosis_del_higado'].mean()
frames = [u,v,w,x,y]
df4 = pd.concat(frames, axis=1)
df4.to_csv(r'fileroot\promedios_enfermedades_por_IDH')
df4.plot(kind="barh",figsize=(8,8), stacked=False)
plt.show()
