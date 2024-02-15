using System;
using System.Text;
using System.Collections.Generic;

public static class ProteinTranslation
{
        public static string[] Proteins(string strand)
        {
            List<string> resultado = new List<string>();
            List<string> subcadenas = new List<string>();

            if (strand.Length % 3 == 0) {
                char[] caracteres = strand.ToCharArray();
                int longitud = caracteres.Length;
                for (int i = 0; i < longitud; i += 3)
                {
                    if (i + 3 <= longitud)
                    {
                        string subcadena = new string(caracteres, i, 3);
                        subcadenas.Add(subcadena);
                    }
                    else
                    {
                        string subcadena = new string(caracteres, i, longitud - i);
                        subcadenas.Add(subcadena);
                    }
                }
            }

          foreach (string subcadena in subcadenas)
            {
                switch (subcadena)
                {
                    case "AUG":
                        resultado.Add("Methionine");
                        continue;
                    case "UUU":
                    case "UUC":
                        resultado.Add("Phenylalanine");
                        continue;
                    case "UUA":
                    case "UUG":
                        resultado.Add("Leucine");
                        continue;
                    case "UCU":
                    case "UCC":
                    case "UCA":
                    case "UCG":
                        resultado.Add("Serine");
                        continue;
                    case "UAU":
                    case "UAC":
                        resultado.Add("Tyrosine");
                        continue;
                    case "UGU":
                    case "UGC":
                        resultado.Add("Cysteine");
                        continue;
                    case "UGG":
                        resultado.Add("Tryptophan");
                        continue;
                    case "UAA":
                    case "UAG":
                    case "UGA":
                        break;
                    default:
                        break;
                }
                return resultado.ToArray();
            }
            return resultado.ToArray();
        }
} 
