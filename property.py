
class Property:
    def __init__(self, square_feet='', bedrooms='', bathrooms='', **kwargs):
        self.bathrooms = bathrooms
        self.bedrooms = bedrooms
        self.square_feet = square_feet

    def display(self):
        print(f'Property Details\n'
              f'=================\n'
              f'Square Feet: {self.square_feet}\n'
              f'Bedrooms: {self.bedrooms}\n'
              f'Bathrooms: {self.bathrooms}\n')

    def prompt_init():
        return dict(
            square_feet = input("Square Feet: "),
            bedrooms = input("Bedrooms: "),
            bathrooms = input("Bathrooms: ")
        )

    prompt_init = staticmethod(prompt_init)

# Instance method ve static method
# Instance methodları sadece ilgili sınıftan instance aldığımızda, instance ismi üzerinden çağırarak kullanabiliriz. Bugüne kadar hep bu yöntemi kullandık. Burada 'display' isimli method yine bu yapıya örnektir.
# Static methodlar ise ilgili sınıfın örneklemi alınmadan direkt sınıf ismi üzerinden çağırırak kullandığımız methodlardır. Python içerisinde built-in olarak bulunan 'math' sınıfı içerisindeki methodları buna örnektir. Burada ise 'prompt_init' methodunu static işaretledik. Böylelikle 'Property' sınıfından örneklem olmadan bu methodu kullanabileceğim.
# Static methodlar kulağa çok hoş gelmektedir. Lakin uygulamada her methodumuzu statik işaretleyemeyiz. Bunun nedeni ise static methodların RAM'in Heap alanındaki yaşama şeklidir. Statik olarak işaretlenmiş her şey RAM in Heap alanında projenin koştuğu server reset edilinceye kadar yaşar. Instance methodlar ise görevlerini icra ettikten sonra Garbage Collector tarafından RAM'in Heap alanından silinirler.
