from django.contrib.auth.models import BaseUserManager

class Gerenciador(BaseUserManager):

    def create_user(self, email, password=None, cpf=None, data_nascimento=None, **extra_fields):
        if not email:
            raise ValueError("O email é obrigatório.")
        if not cpf:
            raise ValueError("O CPF é obrigatório.")
        if not data_nascimento:
            raise ValueError("A data de nascimento é obrigatória.")
        
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            cpf=cpf,
            data_nascimento=data_nascimento,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, cpf=None, data_nascimento=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, cpf, data_nascimento, **extra_fields)
