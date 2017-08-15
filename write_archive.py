import sys

from libcombine import *

def createArchiveExample():
  archive = CombineArchive();

  # add the SED-ML file
  archive.addFile(
    'input_files/main.xml', # source filename
    "main.xml", # target file name
    KnownFormats.lookupFormat("sedml"), # look up identifier for SBML models
    True # mark file as master
    )

  # add the SBML file
  archive.addFile(
    'input_files/mymodel.xml', # source filename
    "mymodel.xml", # target file name
    KnownFormats.lookupFormat("sbml"), # look up identifier for SBML models
    False # set master to false for SBML
    )

  description = OmexDescription();
  description.setAbout("About"); # about the archive itself
  description.setDescription("Test archive");
  description.setCreated(OmexDescription.getCurrentDateAndTime());

  creator = VCard();
  creator.setFamilyName("Medley");
  creator.setGivenName("Kyle");
  creator.setEmail("kylemedley@uw.edu");
  creator.setOrganization("Univ Wash");

  description.addCreator(creator);

  archive.addMetadata(".", description);

  archive.writeToFile("out.omex");


if __name__ == "__main__":
  createArchiveExample()
