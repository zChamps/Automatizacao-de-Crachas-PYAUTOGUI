PT/BR

    Olá! Esse é um projeto de automatização da produção de crachás feito 
inteiramente com Python, ele está subdividido em arquivos onde cada um realiza
determinada parte do processo.

0 - Código onde junta todos os outros módulos e realiza as adaptações necessárias
para o funcionamento correto de todo o processo.

1.1 - Esse módulo realiza a abertura de todos os chamados, tanto admissionais
quanto segunda via no navegador, especificamente para cada quantia de crachás.

1.2 - Esse outro código abre os chamados de determinadas matrículas em particular
onde posso citar quais desejo abrir em específico.

2.1 - Realiza a abertura dos formulários de crachás dentro dos chamados, também
abre as fotos internamente caso tenha e copia o link do formulário para colar no
software do código 3.

2.2 - Caso os chamados tenham sido abertos pelo código 1.2, essa linha de codigo
realiza separadamente a copia dos links dps formulários a fim de colar no código 3.

3 - Nesse código, criei dele um executável, onde recebe o link de todos os
formulários e apartir disso consegue extrair, redimensionar e salvar a foto do
colaborador automaticamente no tamnho e locais adequados. Também extrai a matrícula
dos colaboradores e salva ela em um arquivo separado, que será utilizado posteriormente.

4 - Por sua vez, nesse módulo, o Python pega as matrículas salvas no arquivo 
anterior, e cria um filtro com essas matriculas no sistema da empresa.

5 - Na continuação, ele seleciona somente os dados a serem utilizados nos crachás,
copia e cola eles em uma outra planilha que será a utilizada para a impressão.
Também, quando seleciona os nomes, automaticamente seleciona o primeiro e ultimo
nome, cortando os do meio e colando novamente na planilha, além disso, também
simplifica as diversas escalas dos colaboradores e as cola já simplificadas na
planilha.

6 - No último módulo, ele entra no cadastro de cada funcionário para extrair o 
RG e o número da carteira de trabalho e colar na planilha. Após isso finalizando
o processo de forma inteiramente automática.


EN/US


    Hello! This is a badge production automation project made
entirely with Python, it is subdivided into files where each one performs
certain part of the process.

0 - Code where it joins all the other modules and makes the necessary adaptations
for the correct functioning of the whole process.

1.1 - This module performs the opening of all calls, both admission
as a duplicate in the browser, specifically for each number of badges.

1.2 - This other code opens calls for certain registrations in particular
where I can quote which ones I want to open in specific.

2.1 - Performs the opening of badge forms within the tickets, also
open the photos internally if you have them and copy the form link to paste in the
code software 3.

2.2 - If the calls were opened by code 1.2, this line of code
separately copy the links of the forms in order to paste them in the code 3.

3 - In this code, I created an executable from it, where it receives the link of all
forms and from that it can extract, resize and save the photo of the
employee automatically in the right size and location. It also extracts the registration
collaborators and saves it in a separate file, which will be used later.

4 - In turn, in this module, Python takes the enrollments saved in the file
previous year, and creates a filter with these registrations in the company's system.

5 - Next, he selects only the data to be used in the badges,
copy and paste them into another spreadsheet that will be used for printing.
Also, when selecting names, it automatically selects the first and last
name, cutting the middle ones and pasting them back into the worksheet, in addition, also
simplifies the various scales of employees and glues them already simplified in the
spreadsheet.

6 - In the last module, it enters the registration of each employee to extract the
RG and the work permit number and paste it in the worksheet. After that finishing
the process fully automatically.

