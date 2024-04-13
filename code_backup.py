from codecs import getencoder
import csv
from collections import namedtuple
import itertools
import os
import re
import random


class CreateHumanCharacter():

    def __init__(self, bodyCsvFilePath, faceCsvFilePath):

        #self.mblab_character_list=["m_af01",'m_as01','m_ca01','m_la01','f_af01','f_as01','f_ca01','f_la01']
        self.body_data_list = []
        self.face_data_list = []
        self.body_csv_file = bodyCsvFilePath
        self.face_csv_file = faceCsvFilePath

    def printHumanCharacterFunctionOutput(self, varData:any, title:str):
        print('--------START----------', title, '---------------\n')
        print(varData)
        print('--------END----------', title, '---------------\n')

    def loadBodyParametersFromCSV(self) -> list:
        #this function will load the csv file to a suitable namedtuple to store the values to use further in preceeding functions 
        #output will be a namedtuple storage of the csv list data of body parameters
        with open(self.body_csv_file, mode='r') as data:
            body_parameters_dict = csv.reader(data)
            BodyDataRows = namedtuple('BodyDataRows', next(body_parameters_dict))
            self.body_data_list = [BodyDataRows(*line) for line in body_parameters_dict]
            return self.body_data_list

    # todo - check how to return list of namedtuple 

    def loadFaceParametersFromCSV(self) -> list:
        # 1. this function will load the csv file to a suitable namedtuple to store the values to use further in preceeding functions 
        # 2. output will be a namedtuple storage of the csv list data of face parameters
        with open(self.face_csv_file, mode='r') as data:
            face_parameters_dict = csv.reader(data)
            FaceDataRows = namedtuple('FaceDataRows', next(face_parameters_dict))
            self.face_data_list= [FaceDataRows(*line) for line in face_parameters_dict]
            return self.face_data_list
            
    def fetchBodyShapesByGenderParametersList(self,bodyType: str, gender:str = 'All') -> list :
        # 1. this function will fetch all the body parameters that are required to build a specific body type for a specific gender
        # 2. output is a list of namedtuple which includes ----bodydatalist
        #categories = [BodyDataRowws(*line) for line in self.body_parameters_dict if ]
    
        if gender == 'All':

            return [f for f in self.body_data_list if f.BodyType == bodyType]
        else:
            return [f for f in self.body_data_list if f.BodyType == bodyType and f.Gender == gender]
    
    def fetchFaceParametersByGenderList(self, faceType:str, gender:str = 'All') -> list:
        # 1. this function will fetch all the face parameters that are required to build a specific body type for specific gender
        # 2. output of this function would be a list of namedtuple

        if gender == 'All':

            return [f for f in self.face_data_list if f.FaceType == faceType]
        else:
            return [f for f in self.face_data_list if f.FaceType == faceType and f.Gender == gender]

    def getAllDistinctBodyTypes(self, gender:str) -> list:

        # 1. this function will fetch all distinct body types from the self.body_data_list for all genders 
        # 2. output of this function would be list of strings with different body types  

        bodyTypesList = [record.BodyType for record in self.body_data_list]
        bodyTypesList.sort()
        bodyTypesList = list(k for k,_ in itertools.groupby(bodyTypesList))
        return bodyTypesList

    def getAllDistinctFaceTypes(self, gender:str) -> list:
        # 1. this function will fetch all distinct face types from the self.face_data_list for all genders 
        # 2. output of this function would be list of strings with different face types 
        faceTypesList = [record.FaceType for record in self.face_data_list]
        faceTypesList.sort()
        faceTypesList = list(k for k,_ in itertools.groupby(faceTypesList))
        return faceTypesList 
    
    def getAllMainBodyCategoriesByBodyParameterList(self, bodyParameterList:list) -> list:
        # 1. this function will fetch all the main body categories from bodyParameterList
        # 2. output of this function to return a list of Main Body Categories 
        mainBodyCategoriesList = [record.Category for record in bodyParameterList]
        mainBodyCategoriesList.sort()
        mainBodyCategoriesList = list(k for k,_ in itertools.groupby(mainBodyCategoriesList))
        return mainBodyCategoriesList

    def getAllMainFaceCategoriesByFaceParameterList(self, faceParameterList:list) -> list:
        # 1. this function will fetch all the main face categories from faceParameterList
        # 2. output of this function to return a list of Main Face Categories 
        mainFaceCategoriesList = [record.Category for record in faceParameterList]
        mainFaceCategoriesList.sort()
        mainFaceCategoriesList = list(k for k,_ in itertools.groupby(mainFaceCategoriesList))
        return mainFaceCategoriesList


    #def getAllBodySubCategoriesByBodyParameterList(self, bodyParameterList:list) -> list:
     #   # 1. this function will fetch all the sub body categories from bodyParameterList
        # 2. output of this function to return a list of Sub Body Categories 
      #  subBodyCategoriesList = [record.SubCategory for record in bodyParameterList]
       # subBodyCategoriesList.sort()
        #subBodyCategoriesList = list(k for k,_ in itertools.groupby(subBodyCategoriesList))
        #return subBodyCategoriesList

    #def getAllFaceSubCategoriesByFaceParameterList(self, faceParameterList:list) -> list:
        # 1. this function will fetch all the sub face categories from faceParameterList
        # 2. output of this function to return a list of Sub Face Categories 
     #   subFaceCategoriesList = [record.SubCategory for record in faceParameterList]
      #  subFaceCategoriesList.sort()
       # subFaceCategoriesList = list(k for k,_ in itertools.groupby(subFaceCategoriesList))
        #return subFaceCategoriesList
    
    def updateCharacterPropertiesValuesByBodyTypeGenderCategory(self, bodyType:str, gender:str, category:str) -> None:
        # 1. this function will update all the character Properties values by their body type and gender and categories 
        bodyTypeList = self.fetchBodyShapesByGenderParametersList(bodyType=bodyType, gender=gender)
        filter_categories = [record for record in bodyTypeList if record.Category == category]
        print(filter_categories)
        if len(filter_categories) > 0:
            for item in filter_categories:
                print(str(item.Value))
                
                #bpy.data.objects[character_type]
                #todo- use functions to update value properties in blender
        #else:
         #   print('Nothing to update Check your configuration', bodyType, gender, category)
            
    def mbLabCharacterList(self):
        
        self.mblab_character_list=['m_af01','m_as01','m_ca01','m_la01','f_af01','f_as01','f_ca01','f_la01']
        
        return self.mblab_character_list
    
    def initateMBLabCharacter(self, character_type:str):
        
        self.character_type = random_mblab_character
        #bpy.data.scenes["Scene"].mblab_use_ik = True
        #bpy.data.scenes["Scene"].mblab_use_muscle = True
        #bpy.data.scenes["Scene"].mblab_use_cycles = True
        #bpy.ops.mbast.init_character()
        return self.character_type
    
    def mbLabSceneSetup(self):
        
        #bpy.ops.object.camera_add()
        #bpy.ops.object.light_add(type='SUN')
        
        return True

    def list_of_body_shapes(self):

        list1 = distinct_face_types_list
        list2 = distinct_body_types_list
        all_combinations = []

        list1_permutations = itertools.combinations(list1, len(list2))
        #Get all permutations of `list1` with length 2


        for each_combinaation in list1_permutations:
            zipped = zip(each_combinaation)
            all_combinations.append(list(zipped))

        print(len(all_combinations))
        #print(all_combinations[0])
        combined_list_of_combinations_of_body_and_face_types= [i for i in itertools.product(list1, list2)]

        
        
        return combined_list_of_combinations_of_body_and_face_types
       
    
    def updateCharacterPropertiesValuesByBodyTypeGenderCategory(self, bodyType:str, gender:str, category:str, mb_lab_character:str, combined_list_of_combinations_of_body_and_face_types:list) -> None:
        # 1. this function will update all the character Properties values by their body type and gender and categories 
        bodyTypeList = self.fetchBodyShapesByGenderParametersList(bodyType=bodyType, gender=gender)
        multiple_categories = list(bodyTypeList)
        print(bodyType, gender)
        list_of_combinations_of_body_and_face_types = combined_list_of_combinations_of_body_and_face_types
        #print("test", list_of_combinations_of_body_and_face_types)

        for each_body_shape in list_of_combinations_of_body_and_face_types:

            print(each_body_shape[1])
            #print(each_body_shape[1])
            #print(len(each_body_shape[1]))

            #print("test", list_of_combinations_of_body_and_face_types[0])
            if len(multiple_categories)>0:

                for i in multiple_categories:

                    test = [record for record in multiple_categories if record.Category == category]
                    #print(i.Category)
                    #print(float(i.Value))

                    update_character_value = float(i.Value)
                    #print(update_character_value)
                    category_string = str(i.Category)
                    #print(category_string)

                    if random_mblab_character[0] == 'm' and i.Gender == 'Male':
                        male_filter_categories = [record for record in multiple_categories if record.Category == category and record.Gender == 'Male']
                        #print('male list',male_filter_categories)

                    elif random_mblab_character[0] == 'f' and i.Gender == 'Female' :
                                
                        female_filter_categories = [record for record in multiple_categories if record.Category == category and record.Gender == 'Female']
                        #print('female list', female_filter_categories)
                    else:
                        print('unmatch')

                    #bpy.data.objects[mb_lab_character][category_string] = update_character_value
                    #print(self.character_type)

                    
                    #todo- use functions to update value properties in blender
            else:
                print('Nothing to update Check your configuration', bodyType, gender, category)


    def updateCharacterFacePropertiesValuesByFaceTypeGenderCategory(self, faceType:str, gender:str, category:str, mb_lab_character:str) -> None:

        # 1. this function will update all the character Properties values by their face type and gender and categories

        faceTypeList = self.fetchFaceParametersByGenderList(faceType=faceType, gender=gender)
        multiple_face_categories = list(faceTypeList)
        
        face_types_list = list(self.face_data_list)
        if len(face_types_list) > 0:
            if len(multiple_face_categories)>0:

                for i in multiple_face_categories:
                    test = [record for record in multiple_face_categories if record.Category == category]
                    #print(i.Category)
                    #print(float(i.Value))

                    update_character_value = float(i.Value)
                    #print(update_character_value)
                    category_string = str(i.Category)
                    #print(category_string)

                    if random_mblab_character[0] == 'm' and i.Gender == 'Male':
                        male_filter_face_categories = [record for record in multiple_face_categories if record.Category == category and record.Gender == 'Male']
                        #print('male face categories list',male_filter_face_categories)

                    elif random_mblab_character[0] == 'f' and i.Gender == 'Female' :
                                
                        female_filter_face_categories = [record for record in multiple_face_categories if record.Category == category and record.Gender == 'Female']
                        #print('female list', female_filter_face_categories)
                    else:
                        print('unmatch')

                    #bpy.data.objects[mb_lab_character][category_string] = update_character_value
                    #print(self.character_type)

                    
                    #todo- use functions to update value properties in blender
            else:
                print('Nothing to update Check your configuration', faceType, gender, category)

if __name__ == '__main__':
    os.system('cls') 
    body_parameters_file = "D:/Work/My3D Selfie/Human python try/Revised Character Body parameters.csv"
    face_parameters_file = "D:/Work/My3D Selfie/Human python try/Revised Character Face parameters.csv"
    # create an instance 
    character_objects = CreateHumanCharacter(body_parameters_file, face_parameters_file)
    # call the functions here
    body_parameters_data = character_objects.loadBodyParametersFromCSV()
    #character_objects.printHumanCharacterFunctionOutput(varData=body_parameters_data, title='Body Parameters Data')
    face_parameters_data = character_objects.loadFaceParametersFromCSV()
    #character_objects.printHumanCharacterFunctionOutput(varData=face_parameters_data, title='Face Parameters Data')
    male_rectangular_parameter_list = character_objects.fetchBodyShapesByGenderParametersList(bodyType='Rectangular', gender='Male')
    #character_objects.printHumanCharacterFunctionOutput(varData=male_rectangular_parameter_list, title='Male Rectangular Data')
    face_rectangle_parameters_list = character_objects.fetchFaceParametersByGenderList(faceType='Rectangle', gender='Female')
    #character_objects.printHumanCharacterFunctionOutput(varData=face_rectangle_parameters_list, title='Face Rectangle Parameters Data')
    distinct_body_types_list = character_objects.getAllDistinctBodyTypes(gender='Male')
    #character_objects.printHumanCharacterFunctionOutput(varData=distinct_body_types_list, title='Distinct Body Shapes List')
    distinct_face_types_list = character_objects.getAllDistinctFaceTypes(gender='Male')
    #character_objects.printHumanCharacterFunctionOutput(varData=distinct_face_types_list, title='Distinct Face Shapes List')
    male_rectangular_body_main_categories_list = character_objects.getAllMainBodyCategoriesByBodyParameterList(bodyParameterList=male_rectangular_parameter_list)
    #character_objects.printHumanCharacterFunctionOutput(varData=male_rectangular_body_main_categories_list, title='Male Rectangular Body main categories list')
    female_rectangle_face_main_categories_list = character_objects.getAllMainFaceCategoriesByFaceParameterList(faceParameterList=face_rectangle_parameters_list)
    #character_objects.printHumanCharacterFunctionOutput(varData=female_rectangle_face_main_categories_list, title='Female Face Categories List')
    #male_rectangular_body_sub_categories_list = character_objects.getAllBodySubCategoriesByBodyParameterList(bodyParameterList=male_rectangular_parameter_list)
    #character_objects.printHumanCharacterFunctionOutput(varData=male_rectangular_body_sub_categories_list, title='Male Rectangular Body Sub categories list')
    #female_rectangle_face_sub_categories_list = character_objects.getAllFaceSubCategoriesByFaceParameterList(faceParameterList=face_rectangle_parameters_list)
    #character_objects.printHumanCharacterFunctionOutput(varData=female_rectangle_face_sub_categories_list, title='Female Face  Sub Categories List')
    random_face_type = random.choice(distinct_face_types_list)
    random_body_type = random.choice(distinct_body_types_list)
    random_gender = random.choice(['Male', 'Female'])
    body_type_gender_parameters_list = character_objects.fetchBodyShapesByGenderParametersList(bodyType=random_body_type, gender=random_gender)
    face_type_gender_parameters_list = character_objects.fetchFaceParametersByGenderList(faceType=random_face_type, gender=random_gender)
    character_objects.printHumanCharacterFunctionOutput(varData=face_type_gender_parameters_list, title='Random Face Type Gender Parameter List')
    category_list_by_body_type_gender_parameter_list = character_objects.getAllMainBodyCategoriesByBodyParameterList(bodyParameterList=body_type_gender_parameters_list)
    category_list_by_face_type_gender_parameter_list = character_objects.getAllMainFaceCategoriesByFaceParameterList(faceParameterList=face_type_gender_parameters_list)
    random_category = random.choice(category_list_by_body_type_gender_parameter_list)
    random_face_category = random.choice(category_list_by_face_type_gender_parameter_list)
    mblab_character_list = character_objects.mbLabCharacterList()
    random_mblab_character = random.choice(mblab_character_list)
    #character_objects.printHumanCharacterFunctionOutput(varData=random_mblab_character, title='Random MBLAB Character Title')
    initate_mblab_character = character_objects.initateMBLabCharacter(character_type=random_mblab_character)
    character_objects.mbLabSceneSetup()
    
    #character_objects.printHumanCharacterFunctionOutput(varData=update_character_face_properties_value, title='distinct_body_types_list')
    list_body_shapes_image_rendering = character_objects.list_of_body_shapes()
    #character_objects.printHumanCharacterFunctionOutput(varData=list_body_shapes_image_rendering, title='distinct_body_types_list')
    update_character_face_properties_value = character_objects.updateCharacterFacePropertiesValuesByFaceTypeGenderCategory(faceType=random_face_type, gender=random_gender, category=random_face_category, mb_lab_character=random_mblab_character)
    update_character_properties_value = character_objects.updateCharacterPropertiesValuesByBodyTypeGenderCategory(bodyType=random_body_type, gender=random_gender, category=random_category, mb_lab_character=random_mblab_character, combined_list_of_combinations_of_body_and_face_types=list_body_shapes_image_rendering)
