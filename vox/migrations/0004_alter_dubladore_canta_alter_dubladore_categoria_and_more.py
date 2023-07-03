# Generated by Django 4.2.2 on 2023-06-21 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vox', '0003_alter_dubladore_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dubladore',
            name='canta',
            field=models.CharField(choices=[('S', 'Sim'), ('Não', 'Nâo')], default='Não', max_length=3),
        ),
        migrations.AlterField(
            model_name='dubladore',
            name='categoria',
            field=models.CharField(choices=[('ADULTA_MASCULINA_PESADA', 'Adulta Masculina Pesada'), ('INFANTIL_FEMININA', 'Infantil Feminina'), ('IDOSA_FEMININA_PESADA', 'Idosa Feminina Pesada'), ('INFANTIL_MASCULINA', 'Infantil Masculina'), ('ADULTA_FEMININA_LEVE', 'Adulta Feminina Leve'), ('JOVEM_FEMININA_LEVE', 'Jovem Feminina Leve'), ('ADULTA_MASCULINA', 'Adulta Masculina'), ('IDOSA_MASCULINA_LEVE', 'Idosa Masculina Leve'), ('ADULTA_FEMININA_PESADA', 'Adulta Feminina Pesada'), ('MEIA_IDADE_MASCULINA', 'Meia Idade Masculina'), ('JOVEM_FEMININA', 'Jovem Feminina'), ('JOVEM_MASCULINA_LEVE', 'Jovem Masculina Leve'), ('MEIA_IDADE_FEMININA', 'Meia Idade Feminina'), ('IDOSA_FEMININA_LEVE', 'Idosa Feminina Leve'), ('JOVEM_FEMININA_PESADA', 'Jovem Feminina Pesada'), ('IDOSA_FEMININA', 'Idosa Feminina'), ('ADOLESCENTE_FEMININA', 'Adolescente Feminina'), ('IDOSA_MASCULINA', 'Idosa Masculina'), ('ADULTA_MASCULINA_LEVE', 'Adulta Masculina Leve'), ('JOVEM_MASCULINA', 'Jovem Masculina'), ('ADULTA_FEMININA', 'Adulta Feminina'), ('ADOLESCENTE_MASCULINA', 'Adolescente Masculina'), ('JOVEM_MASCULINA_PESADA', 'Jovem Masculina Pesada'), ('IDOSA_MASCULINA_PESADA', 'Idosa Masculina Pesada')], max_length=2500),
        ),
        migrations.AlterField(
            model_name='dubladore',
            name='genero',
            field=models.CharField(choices=[('Homem Cis', 'Homem Cis'), ('Homem Trans', 'Homem Trans'), ('intersexo', 'intersexo'), ('Mulher Cis', 'Mulher Cis'), (' Mulher Trans', ' Mulher Trans'), ('Não Binário', 'Não Binário')], max_length=1000),
        ),
        migrations.AlterField(
            model_name='dubladore',
            name='pcd',
            field=models.CharField(choices=[('S', 'Sim'), ('Não', 'Nâo')], default='Não', max_length=3),
        ),
    ]
