from rest_framework import serializers

from .models import *
# from django.contrib.auth import get_user_model
class UserSerializer(serializers.ModelSerializer):
    
    
    def create(self, validated_data):
     
        #    user = User.objects.create(
        #         email=validated_data['email'],
        #         first_name=validated_data['first_name'],
        #         last_name=validated_data['last_name'],
        #         education=validated_data['education'],
        #         profile_picture=validated_data['profile_picture'], 
            # )
            if validated_data['user_type']=='freelancer':
                freelancer=Freelancer.objects.create_freelancer(**validated_data
                )
                return validated_data
            
            elif validated_data['user_type']=='client':
                # breakpoint()
                client=Client.objects.create_client(**validated_data)
                
                return validated_data
            
            elif validated_data['user_type']=='admin':
                admin=User.objects.create_superuser()
                return admin
            # validated_data.set_password(validated_data['password'])
            # validated_data.save()
            return validated_data
        
           
    

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {'last_login': {'write_only': True},'password':{'write_only':True}}
        
class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Education
        fields='__all__'
        
class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Certification
        fields='__all__'
class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Portfolio
        fields='__all__'
        
class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Skills
        fields='__all__'

class FreelancerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    skills = SkillsSerializer()
    certification = CertificationSerializer()
    portfolio = PortfolioSerializer()
    

    
    
    # def create(self, validated_data):
    #     freelancer=Freelancer.objects.create(
            
    #         user=validated_data['user'],
    #         age=validated_data['age'],
    #         skills=validated_data['skills'],
    #         certification=validated_data['certification'],
    #         portfolio=validated_data['portfolio'],
    #         country=validated_data['country'],
    #         linkedin=validated_data['linkedin_url'],
    #         behance=validated_data['behance_url'],
    #         facebook_url=validated_data['facebook_url']
    #     )
    #     return freelancer
      
    class Meta:
        model=Freelancer
        fields="__all__"
        
class ReadUserSerializer(serializers.ModelSerializer):
    freelancer=FreelancerSerializer(read_only=True)
    class Meta:
        model=Freelancer
        fields='__all__'
        
